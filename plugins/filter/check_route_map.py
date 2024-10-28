def svi_to_vlan(vlan_intf):
    # Convert vlan_interfaces to a list of valid vlan numbers
    # [int(svi['name'][4:]) for svi in vlan_intf]
    vlans = []
    for svi in vlan_intf:
        vlans.append(int(svi['name'].replace('Vlan','')))
    return vlans

def check_route_map(route_map_sequence, valid_vlan_svis):
    """Checks if a route map sequence should be rendered based on its matched SVIs."""
    vlan_svi_nums = svi_to_vlan(valid_vlan_svis)

    for match_rule in route_map_sequence["match"]:
        if match_rule.startswith("interface Vlan"):
            vlan_number = match_rule.split("interface Vlan")[1].strip()

            if vlan_number.isdigit():
                vlan_number = int(vlan_number)
                if vlan_number in vlan_svi_nums:
                    return True
            return False

    return True

class FilterModule(object):
    def filters(self):
        return {
            'check_route_map': check_route_map,
        }