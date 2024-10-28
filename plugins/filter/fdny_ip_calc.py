import ipaddress

# Define order of boroughs and VRFs
co_order = ['BK', 'QN', 'MN', 'BX', 'SI']  # Borough codes
vrf_order = ['VRFA', 'VRFB', 'VRFC', 'VRFD', 'VRFE', 'VRFM', 'VRFT-DC', 'VRFT-CE', 'MDMZ']  # VRF names

# Define IP address pools for different network segments
mpls_uplinks = ipaddress.IPv4Network('172.26.0.0/16')
velo_uplinks = ipaddress.IPv4Network('172.17.0.0/16')
mdmz_uplinks = ipaddress.IPv4Network('172.27.32.0/19')
mlag_addresses = ipaddress.IPv4Network('172.27.64.0/19')

# Define loopback and management addresses for each borough
loop100_addresses = {
    'BK': ipaddress.IPv4Address('172.22.1.0'),
    'QN': ipaddress.IPv4Address('172.22.17.0'),
    'MN': ipaddress.IPv4Address('172.22.33.0'),
    'BX': ipaddress.IPv4Address('172.22.49.0'),
    'SI': ipaddress.IPv4Address('172.22.65.0'),
}
ma1_addresses = {
    'BK': ipaddress.IPv4Address('192.168.32.0'),
    'QN': ipaddress.IPv4Address('192.168.36.0'),
    'MN': ipaddress.IPv4Address('192.168.40.0'),
    'BX': ipaddress.IPv4Address('192.168.44.0'),
    'SI': ipaddress.IPv4Address('192.168.48.8'),
}


def get_subnet_from_pool(pool: ipaddress.IPv4Address,
                         prefixlen: int,
                         subnet_offset: int) -> ipaddress.IPv4Network:
    """
    Generate a subnet from a given CIDR IP pool.

    :param pool: IP pool to retrieve subnet from (IPv4Network or IPv4Address)
    :param prefixlen: Prefix length of the subnet to retrieve
    :param subnet_offset: Offset of the subnet from the first subnet of the given prefix length

    :return: An IPv4Network object representing the subnet
    :raises ValueError: If the pool's prefix length is less than the requested prefix length
    """
    prefixlen_diff = prefixlen - pool.prefixlen
    if prefixlen_diff < 0:
        raise ValueError(f"IP pool's prefix length ({pool.prefixlen}) is less "
                         f"than the prefix length of the subnet requested ({prefixlen}).")

    subnet_size = (int(pool.hostmask) + 1) >> prefixlen_diff

    subnet = ipaddress.ip_network(
        (int(pool.network_address) + subnet_offset * subnet_size, prefixlen))

    return subnet


def get_offsets(site_id):
    """
    Calculate offsets for a given site ID

    :param site_id: Site identifier (e.g., 'BKFDS001')
    :return: Tuple of (county offset, site offset)
    """
    office_code = site_id[:2]
    if office_code not in co_order:
        raise ValueError(f"CO code: {office_code} not found in {site_id}")
    co_offset = co_order.index(office_code)
    site_offset = int(site_id[-3:]) - 1  # Adjusting to zero-based indexing
    return co_offset, site_offset


def fdny_ip_mlag(siteid, l3=False, ibgp=False, as_number=0):
    """
    Generate MLAG IP address for a given site

    :param siteid: Site identifier
    :param l3_ibgp: Boolean flag for L3 iBGP
    :return: MLAG IP address subnet
    """
    co_offset, site_offset = get_offsets(siteid)
    co_mlag_range = get_subnet_from_pool(mlag_addresses, 22, co_offset)
    site_mlag_range = get_subnet_from_pool(co_mlag_range, 30, site_offset)
    l3_ibgp_offset = 1 if l3 or ibgp else 0
    l3_ibgp = get_subnet_from_pool(site_mlag_range, 31, l3_ibgp_offset)
    if not ibgp:
        return l3_ibgp
    elif ibgp and as_number == 1:
        return l3_ibgp.network_address + 0
    elif ibgp and as_number == 2:
        return l3_ibgp.network_address + 1


def fdny_ip_uplink(siteid, as_number, vrf, uplink_type, self_ip=True):
    """
    Generate uplink IP address for a given site

    :param siteid: Site identifier
    :param as_number: AS number (1 or 2)
    :param vrf: VRF name
    :param uplink_type: Type of uplink ('mpls' or 'velo')
    :param self_ip: Boolean flag for self IP
    :return: Uplink IP address
    """
    co_offset, site_offset = get_offsets(siteid)
    if as_number not in [1, 2]:
        raise ValueError(f"AS device number should be 1 or 2. Got {as_number} instead")
    if vrf not in vrf_order:
        raise ValueError(f"VRF type should be one of {vrf_order}.\n Got {vrf} instead")
    vrfid = vrf_order.index(vrf)

    if uplink_type == "mpls":
        uplinks_range = mpls_uplinks
    elif uplink_type == "velo":
        uplinks_range = velo_uplinks
    else:
        raise ValueError(f"Uplink type should be 'mpls' or 'velo'. Got {uplink_type} instead")

    # Get all /19 subnets within the /16 network and add entries to vrfs except MDMZ vrf
    if vrf == 'MDMZ':
        if uplink_type == 'velo':
            raise ValueError(f"'velo' uplink type does not have VRF 'MDMZ'")
        else:
            vrf_subnet = mdmz_uplinks
    else:
        vrf_subnet = get_subnet_from_pool(uplinks_range, 19, vrfid)

    co_subnet = get_subnet_from_pool(vrf_subnet, 22, co_offset)
    site_subnet = get_subnet_from_pool(co_subnet, 30, site_offset)

    self_offset = 1 if self_ip else 0

    return site_subnet.network_address + (as_number-1)*2 + self_offset


def fdny_ip_lo100(siteid, as_number):
    """
    Generate loopback IP address for a given site

    :param siteid: Site identifier
    :param as_number: AS number (1 or 2)
    :return: Loopback IP address
    """
    co_offset, site_offset = get_offsets(siteid)
    as_number = int(as_number)
    if as_number not in [1, 2]:
        raise ValueError(f"AS device number should be 1 or 2. Got {as_number} instead")

    # Using 2 IP addresses per site from the assigned /24
    return loop100_addresses[siteid[:2]] + site_offset*2 + as_number-1


def fdny_ip_ma1(siteid, as_number, self_ip=True):
    """
    Generate management IP address for a given site

    :param siteid: Site identifier
    :param as_number: AS number (1 or 2)
    :param self_ip: Boolean flag for self IP
    :return: Management IP address
    """
    co_offset, site_offset = get_offsets(siteid)
    if as_number not in [1, 2]:
        raise ValueError(f"AS device number should be 1 or 2. Got {as_number} instead")
    if as_number == 1:
        device_offset = 1 if self_ip else 0
    elif as_number == 2:
        device_offset = 3 if self_ip else 2

    # Using 4 IP addresses per site from the assigned /22
    return ma1_addresses[siteid[:2]] + site_offset*4 + device_offset


# Uncomment the following block to test IP uplink generation for a specific site
# for vrf in vrf_order:
#     sid = 'QNFDS032'
#     print(fdny_ip_uplink('QNFDS032', 1, vrf, 'velo'))
#     print(fdny_ip_uplink('QNFDS032', 2, vrf, 'velo'))
#     print(fdny_ip_uplink('QNFDS032', 1, vrf, 'velo', self_ip=False))
#     print(fdny_ip_uplink('QNFDS032', 2, vrf, 'velo', self_ip=False))

class FilterModule(object):
    """
    Ansible filter module class that provides custom filters for IP address calculation.
    """
    def filters(self):
        """
        Return the custom filters available in this module.

        :return: Dictionary of filter names and corresponding filter functions
        """
        return {
            'fdny_ip_mlag': fdny_ip_mlag,
            'fdny_ip_uplink': fdny_ip_uplink,
            'fdny_ip_lo100': fdny_ip_lo100,
            'fdny_ip_ma1': fdny_ip_ma1,
        }
