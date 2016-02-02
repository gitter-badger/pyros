#!/usr/bin/env python
from __future__ import absolute_import

# Unit test import (  will emulate ROS setup if needed )
import nose
import time



try:
    from pyros.baseinterface import DiffTuple
    from pyros.rosinterface import RosInterface, TopicBack
except ImportError as exc:
    import os
    import pyros.rosinterface
    import sys
    sys.modules["pyros.rosinterface"] = pyros.rosinterface.delayed_import_auto(base_path=os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..', '..'))
    from pyros.baseinterface import DiffTuple
    from pyros.rosinterface import RosInterface, TopicBack

import rospy
import roslaunch
import rosnode
from std_msgs.msg import String, Empty
from std_srvs.srv import Empty as EmptySrv, Trigger

from pyros.rosinterface.rostests import Timeout, TestRosInterface

# useful test tools
from pyros_setup import rostest_nose
import unittest

launch = None
# test node process not setup by default (rostest dont need it here)
empty_srv_process = None
trigger_srv_process = None


# This should have the same effect as the <name>.test file for rostest. Should be used only by nose ( or other python test tool )
# CAREFUL with comments, copy paste mistake are real...
# CAREFUL dont use assertFalse -> easy to miss when reviewing code
def setup_module():
    if not rostest_nose.is_rostest_enabled():
        rostest_nose.rostest_nose_setup_module()


def teardown_module():
    if not rostest_nose.is_rostest_enabled():

        rospy.signal_shutdown('test complete')

        rostest_nose.rostest_nose_teardown_module()


# Very basic echo service implementation for tests
def srv_cb(req):
    return req.request


# Testing with Connection Cache
@nose.tools.istest
class TestRosInterfaceCache(TestRosInterface):
    def setUp(self):
        self.connection_cache_spin_freq = 1  # change this to test different spin speed for the connection cache node
        rospy.set_param("/connection_cache/spin_freq", self.connection_cache_spin_freq)
        self.connection_cache_node = roslaunch.core.Node('rocon_python_comms', 'connection_cache.py', name='connection_cache',
                                                         remap_args=[('~list', rospy.resolve_name('~connections_list')),
                                                                     ('~diff', rospy.resolve_name('~connections_diff'))])
        # Easier to remap the node topic to the proxy ones, instead of the opposite, since there is no dynamic remapping.
        # However for normal usecase, remapping the proxy handles is preferable.
        try:
            self.connection_cache_proc = TestRosInterface.launch.launch(self.connection_cache_node)
        except roslaunch.RLException as rlexc:
            raise nose.SkipTest("Connection Cache Node not found (part of rocon_python_comms pkg). Skipping test.")

        assert self.connection_cache_proc.is_alive()

        # wait for node to be started
        node_api = None
        with Timeout(5) as t:
            while not t.timed_out and node_api is None:
                node_api = rosnode.get_api_uri(rospy.get_master(), 'connection_cache')

        assert node_api is not None  # make sure the connection cache node is started before moving on.

        self.strpub = rospy.Publisher('/test/string', String, queue_size=1)
        self.emppub = rospy.Publisher('/test/empty', Empty, queue_size=1)

        self.interface = RosInterface(True)

    def tearDown(self):
        self.interface = None

        self.connection_cache_proc.stop()
        while self.connection_cache_proc.is_alive():
            time.sleep(0.2)  # waiting for cache node to die
        assert not self.connection_cache_proc.is_alive()
        time.sleep(1)  # TODO : investigate : we shouldnt need this


    # explicitely added here only needed to help the debugger.
    # This will fail because of https://github.com/ros/ros_comm/issues/111
    # The topic from previous test is still registered on master...
    def test_topic_expose_appear_update(self):
        super(TestRosInterfaceCache, self).test_topic_expose_appear_update()

        
if __name__ == '__main__':

    # Note : Tests should be able to run with nosetests, or rostest ( which will launch nosetest here )
    rostest_nose.rostest_or_nose_main('test_ros_interface', 'test_all', TestRosInterface)

