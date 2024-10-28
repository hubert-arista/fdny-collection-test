
def raise_stack_type_error(stack_type):
    raise ValueError(f"Invalid stack_type: {stack_type}")

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
            'raise_stack_type_error': raise_stack_type_error,
        }