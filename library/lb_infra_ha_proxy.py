#!/bin/env python
from ansible.module_utils.basic import *


def _haproxy_item(host, weight, app_name):
    return {
        "host": host, "weight": str(weight) + "%", "backend": app_name + "_be",
        "socket": "/var/lib/haproxy/" + app_name + ".stats"
    }


if __name__ == "__main__":
    fields = {
        "java_blauwrood_servers": {"java_blauwrood_servers": True, "type": "list"},
        "php_blauwrood_servers": {"php_blauwrood_servers": True, "type": "list"},
        "weight": {"required": True},
        "color": {"required": True},
        "app_name": {"required": True},
        "app_type": {"required": True}
    }
    module = AnsibleModule(argument_spec=fields)
    java_servers = [s["label"] for s in module.params["java_blauwrood_servers"]]
    php_servers = [s["label"] for s in module.params["php_blauwrood_servers"]]
    weight = module.params["weight"]
    weight = int(weight[:-1]) if weight.endswith("%") else int(weight)
    color = module.params["color"].lower()
    app_name = module.params["app_name"].lower()
    app_type = module.params["app_type"].lower()

    servers = java_servers if app_type == "java" else php_servers
    other_weight = 100 - weight
    red_servers = [s for s in servers if s.upper().endswith("ROOD")]
    blue_servers = [s for s in servers if s.upper().endswith("BLAUW")]

    red_weight = weight if color == "rood" else other_weight
    blue_weight = weight if color == "blauw" else other_weight

    red_items = [_haproxy_item(s, red_weight, app_name) for s in red_servers]
    blue_items = [_haproxy_item(s, blue_weight, app_name) for s in blue_servers]
    module.exit_json(haproxy_items=red_items + blue_items)
