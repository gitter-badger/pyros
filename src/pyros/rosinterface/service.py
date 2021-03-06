from __future__ import absolute_import


import roslib
import rospy

from importlib import import_module
from collections import OrderedDict

from .message_conversion import get_msg, get_msg_dict


# outputs message structure as string (useful ?)
def get_service_srv(service):
    return '\n'.join([
        get_msg(service.rostype_req),
        '---',
        get_msg(service.rostype_resp),
    ])


# outputs message structure as dict
def get_service_srv_dict(service):
    return get_msg_dict(service.rostype_req), get_msg_dict(service.rostype_resp)


class ServiceBack(object):
    """
    ServiceBack is the class handling conversion from Python API to ROS Service
    """
    def __init__(self, service_name, service_type):
        self.name = service_name
        # getting the fullname to make sure we start with /
        self.fullname = self.name if self.name.startswith('/') else '/' + self.name

        service_type_module, service_type_name = tuple(service_type.split('/'))
        roslib.load_manifest(service_type_module)
        srv_module = import_module(service_type_module + '.srv')

        self.rostype_name = service_type
        self.rostype = getattr(srv_module, service_type_name)
        self.rostype_req = getattr(srv_module, service_type_name + 'Request')
        self.rostype_resp = getattr(srv_module, service_type_name + 'Response')

        self.srvtype = get_service_srv_dict(self)
        #rospy.logwarn('srvtype : %r', self.srvtype)

        self.proxy = rospy.ServiceProxy(self.name, self.rostype)

    def cleanup(self):
        pass

    def asdict(self):
        """
        Here we provide a dictionary suitable for a representation of the Topic instance
        the main point here is to make it possible to transfer this to remote processes.
        We are not interested in pickleing the whole class with Subscriber and Publisher
        :return:
        """

        return OrderedDict({
            'name': self.name,
            'fullname': self.fullname,
            'rostype_name': self.rostype_name,
            'srvtype': self.srvtype,
        })

    def call(self, rosreq = None):
#       rosreq = self.rostype_req()
#       if use_ros:
#           rosreq.deserialize(req)
#       else:
#           msgconv.populate_instance(req, rosreq)

        fields = []
        if rosreq:
            for slot in rosreq.__slots__:
                fields.append(getattr(rosreq, slot))
            fields = tuple(fields)

        return self.proxy(*fields)
