import hier_config

def main(old_config_path, new_config_path):

    ignore_cmds = [
        'no crypto',
        'no interface Gi',
        'no interface Te',
        'no interface Tw',
        'no interface Fo',
        'no interface Ap',
        'no interface Hu',
        'no banner',
        'banner'
    ]


    host = hier_config.Host('example_hostname', 'ios', {})
    host.load_running_config(old_config_path)
    host.load_generated_config(new_config_path)
    delta = host.remediation_config()

    filtered_diff_lines = [
        Hconfline.cisco_style_text() for Hconfline in delta.all_children_sorted()
        if not any(Hconfline.text.startswith(cmd) for cmd in ignore_cmds)
    ]


    pass


if __name__ == '__main__':
    with open('./intended/QN/QNFDS008-E317/QNFDS008-E317-CS01.cfg') as f:
        new = f.read()
    with open('./.local/runn.txt') as f:
        old = f.read()
    main(old, new)
