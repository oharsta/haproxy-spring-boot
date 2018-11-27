#!/bin/env python
from ansible.module_utils.basic import *
import os, json
import re, sys


def first_prog(text):
    text1 = "Hello " + text
    return text1


if __name__ == '__main__':
    print("hello")
    fields = {
        "yourName": {"required": True, "type": "str"}
    }
    module = AnsibleModule(argument_spec=fields)
    print(list(module.params.keys))
    yourName = os.path.expanduser(module.params['yourName'])
    newName = first_prog(yourName)
    module.exit_json(msg=newName)
