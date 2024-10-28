import yaml


def fdny_inv_to_cvp(vars):

    all_hosts = vars['groups']['FIREHOUSE']

    output_data = {
        'CVP_CONFIGLET' : {},
        'CVP_CONTAINERS': {},
        'CVP_DEVICES': [],
    }

    def read_file_content(filepath):
        with open(filepath, 'r') as file:
            return file.read()

    for host in all_hosts:
        co_id = host[:2]
        siteidlong = host[:13]
        sitenum = host[5:8]

        config_path = f'{vars["inventory_dir"]}/../intended/{co_id}/{siteidlong}/{host}.cfg'
        contname = f'{co_id}{sitenum}.FH.FDNY'
        parentcontname = f'{co_id}.FH.FDNY'
        serial_no = vars['hostvars'][host]['serial_number']

        output_data['CVP_CONFIGLET'][vars['avd_configlet_prefix']+host] = read_file_content(config_path)
        output_data['CVP_CONTAINERS'][contname] = {'parentContainerName': parentcontname}
        output_data['CVP_DEVICES'].append({
            'serialNumber': serial_no,
            'parentContainerName': contname,
            'configlets': [vars['avd_configlet_prefix']+host]
        })

    return output_data

class FilterModule(object):
    def filters(self):
        return {
            'fdny_inv_to_cvp': fdny_inv_to_cvp,
        }
