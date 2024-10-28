import os
import re
import yaml
from typing import List
from ansible.module_utils.basic import AnsibleModule


def load_yaml_file(path):
    """Load YAML file from the specified path."""
    if not os.path.exists(path):
        return {"_cisco_crypto": None}  # Handles KeyError (during compare) if file does not exist

    with open(path, 'r') as file:
        try:
            return yaml.safe_load(file) or {}  # Handle empty files
        except yaml.YAMLError as e:
            return None


def save_yaml_file(path, crypto_config):
    """Save content back to the YAML file. Caution: Uses write instead of YAML dump"""
    with open(path, 'w') as file:
        content = (
            "_cisco_crypto: |\n  "+
            "\n  ".join(crypto_config.splitlines())+
            "\n"
        )
        file.write(content)


def main():
    """Cisco fetch crypto module.

    :param running_config: String representation of running configuration.
    :return: crypto_lines: List[str] of all crypto-related configruation.
    """

    module_args = dict(
        running_config=dict(type='str', required=True),
        site=dict(type='str', required=True),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True  # Allows the module to support dry-run mode
    )

    running_config = module.params["running_config"]
    site = module.params["site"]
    crypto_var_path = f"../inventory/group_vars/{site}/CRYPTO.yml"

    # Load existing YAML file
    current_data = load_yaml_file(crypto_var_path)

    if current_data is None:
        module.fail_json(msg="Failed to load YAML file.")

    if '_cisco_crypto' not in current_data.keys():
        module.fail_json(msg="Failed to load YAML file. KeyError: '_cisco_crypto' does not exist")

    # Extract crypto pki sections from running config
    crypto_lines = re.findall(r'crypto pki.*\n(?:\s+.+\n)*', running_config)
    crypto_config = '!\n'.join(crypto_lines)

    # Compare current data with the new data
    if current_data['_cisco_crypto'] == crypto_config:
        # No change needed
        module.exit_json(changed=False, msg="YAML file is already up-to-date", data=current_data)

    # If check_mode is enabled, do not write changes, only simulate
    if module.check_mode:
        module.exit_json(changed=True, msg="YAML file would be updated (check mode)", diff=dict(before=current_data['_cisco_crypto'], after=crypto_config))

    # Update the YAML file with new data
    save_yaml_file(crypto_var_path, crypto_config)

    # Return the result with 'changed' status
    module.exit_json(changed=True, msg="YAML file updated", diff=dict(before=current_data['_cisco_crypto'], after=crypto_config))


if __name__ == '__main__':
    main()
