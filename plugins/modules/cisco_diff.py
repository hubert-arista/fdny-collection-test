from ansible.module_utils.basic import AnsibleModule
from ciscoconfparse2.ciscoconfparse2 import Diff

def run_module():
    """Cisco config diff module."""

    module_args = dict(
        old_config=dict(type='str', required=True),
        new_config=dict(type='str', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    old_config = module.params["old_config_path"]
    new_config = module.params["new_config_path"]

        
    try:
        diff = Diff(old_config=old_config, new_config=new_config)
    except:
        raise ValueError(f"Invalid input error: Either old_config or new_config is invalid.")
    
    diff_text = "\n".join(diff.get_diff())
    
    result = dict(
        diff_result=diff_text,
        exists=True
    )

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()