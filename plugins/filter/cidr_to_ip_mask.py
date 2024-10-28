import ipaddress

# Define the filter function
def cidr_to_ip_mask(cidr: str):
    """Converts IPv4 interface from CIDR format to IP address and mask format."""
    try:
        # Convert the CIDR to an IPv4 network object
        network = ipaddress.IPv4Interface(cidr)
        
        # Extract the IP address and subnet mask
        ip_address = network.ip
        subnet_mask = network.netmask
        
        # Return the IP and subnet mask as a single string
        return f"{ip_address} {subnet_mask}"
    except ValueError:
        raise ValueError(f"Invalid CIDR: {cidr}")

class FilterModule(object):
    def filters(self):
        return {
            'cidr_to_ip_mask': cidr_to_ip_mask,
        }
