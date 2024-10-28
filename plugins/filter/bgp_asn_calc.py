def fdny_calc_asn(siteid, remote="self"):
    asn_offset_globals = {
        'BK': 50000,
        'QN': 60000,
        'MN': 70000,
        'BX': 80000,
        'SI': 90000,
    }

    # Extract the office code from the siteid (first 2 characters)
    office_code = siteid[:2]

    # Extract the offset value (last 3 characters)
    offset_value = int(siteid[-3:])

    # Get the ASN offset for the office code
    if office_code in asn_offset_globals:
        asn_offset = asn_offset_globals[office_code]
    else:
        raise ValueError(f"CO code: {office_code} not found in {siteid}")

    # Get the Velocloud AS number
    if remote == "velo":
        asn_offset = asn_offset + 1000

    # Calculate the BGP ASN
    bgp_asn = 4200000000 + asn_offset + offset_value

    return bgp_asn

class FilterModule(object):
    def filters(self):
        return {
            'fdny_calc_asn': fdny_calc_asn,
        }
