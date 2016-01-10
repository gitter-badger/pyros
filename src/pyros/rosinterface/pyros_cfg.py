## *********************************************************
##
## File autogenerated for the pyros package
## by the dynamic_reconfigure package.
## Original cfg file contents :
##  ----
## #! /usr/bin/env python
## PACKAGE='pyros'
##
## from dynamic_reconfigure.parameter_generator_catkin import *
##
## gen = ParameterGenerator()
## gen.add("topics", str_t, 0, "Topics", "['/turtle1/pose', '/turtle1/cmd_vel']")
## gen.add("services", str_t, 0, "Services", "[]")
## gen.add("params", str_t, 0, "Parameters", "[]")
## gen.add("enable_rocon", bool_t, 0, "Enable Rocon", False)
## gen.add("rapps_namespaces", str_t, 0, "Rapps Namespaces", "[]")
## gen.add("interactions", str_t, 0, "Interactions", "[]")
##
## exit(gen.generate(PACKAGE, "pyros", "Pyros"))
##  ----
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {
    'upper': 'DEFAULT',
    'lower': 'groups',
    'srcline': 233,
    'name': 'Default',
    'parent': 0,
    'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py',
    'cstate': 'true',
    'parentname': 'Default',
    'class': 'DEFAULT',
    'field': 'default',
    'state': True,
    'parentclass': '',
    'groups': [],
    'parameters': [
        {
            'srcline': 262,
            'description': 'Topics',
            'max': '',
            'cconsttype': 'const char * const',
            'ctype': 'std::string',
            'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py',
            'name': 'topics',
            'edit_method': '',
            'default': "['/turtle1/pose', '/turtle1/cmd_vel']",
            'level': 0,
            'min': '',
            'type': 'str'
        }, {
            'srcline': 262,
            'description': 'Services',
            'max': '',
            'cconsttype': 'const char * const',
            'ctype': 'std::string',
            'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py',
            'name': 'services',
            'edit_method': '',
            'default': '[]',
            'level': 0,
            'min': '',
            'type': 'str'
        }, {
            'srcline': 262,
            'description': 'Parameters',
            'max': '',
            'cconsttype': 'const char * const',
            'ctype': 'std::string',
            'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py',
            'name': 'params',
            'edit_method': '',
            'default': '[]',
            'level': 0,
            'min': '',
            'type': 'str'
        }, {
            'srcline': 262,
            'description': 'Enable Rocon',
            'max': True,
            'cconsttype': 'const bool',
            'ctype': 'bool',
            'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py',
            'name': 'enable_rocon',
            'edit_method': '',
            'default': False,
            'level': 0,
            'min': False,
            'type': 'bool'
        }, {
            'srcline': 262,
            'description': 'Rapps Namespaces',
            'max': '',
            'cconsttype': 'const char * const',
            'ctype': 'std::string',
            'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py',
            'name': 'rapps_namespaces',
            'edit_method': '',
            'default': '[]',
            'level': 0,
            'min': '',
            'type': 'str'
        }, {
            'srcline': 262,
            'description': 'Interactions',
            'max': '',
            'cconsttype': 'const char * const',
            'ctype': 'std::string',
            'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py',
            'name': 'interactions',
            'edit_method': '',
            'default': '[]',
            'level': 0,
            'min': '',
            'type': 'str'
        }
    ],
    'type': '',
    'id': 0
}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

