iosxe_cli_config_gen
====================

iosxe_cli_config_gen role for FDNY customer project.

### Modification:

1. Update alias to alias exec in template
2. Update snmp user jinja
3. Update banner jinja

### Notes

- `snmp-server user` commands do not show up in running config which will always produce a diff
- also `snmp-server user` is not defined in jinja template
- cannot create standard access-lists

### Errors

1. Error executing playbook. Why a connection error. Do we not do delegate to localhost or is it related to gather facts/parmiko/pylib-ssh

```bash
(.venv) rahulpurohit@Rahuls-MacBook-Pro firehouse-fdny-github % make build-cisco
ansible-playbook playbooks/build-cisco.yml --skip-tags documentation
/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/.venv/lib/python3.9/site-packages/paramiko/pkey.py:100: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from this module in 48.0.0.
  "cipher": algorithms.TripleDES,
/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/.venv/lib/python3.9/site-packages/paramiko/transport.py:259: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from this module in 48.0.0.
  "class": algorithms.TripleDES,
all /Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/inventory

PLAY [Run Cisco AVD] ***************************************************************************************************************************************************************************************************************************************************************************************************************************************************

TASK [Extract vars from hostname to be used in custom filters] *********************************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:19:46 -0400 (0:00:00.224)       0:00:00.224 ******
ok: [QNFDS012-E294-CS01]
[WARNING]: ansible-pylibssh not installed, falling back to paramiko
ok: [QNFDS003-E285-CS01]

TASK [Set custom output directory] *************************************************************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:19:48 -0400 (0:00:01.723)       0:00:01.947 ******
ok: [QNFDS003-E285-CS01]
fatal: [QNFDS012-E294-CS01]: FAILED! =>
  msg: |-
    /Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/.venv/lib/python3.9/site-packages/paramiko/pkey.py:100: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from this module in 48.0.0.
      "cipher": algorithms.TripleDES,
    /Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/.venv/lib/python3.9/site-packages/paramiko/transport.py:259: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from this module in 48.0.0.
      "class": algorithms.TripleDES,
    Traceback (most recent call last):
      File "/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/.venv/lib/python3.9/site-packages/ansible/module_utils/connection.py", line 207, in send
        sf.connect(self.socket_path)
    ConnectionRefusedError: [Errno 61] Connection refused

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/.venv/lib/python3.9/site-packages/ansible/cli/scripts/ansible_connection_cli_stub.py", line 315, in main
        conn.set_options(direct=options)
      File "/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/.venv/lib/python3.9/site-packages/ansible/module_utils/connection.py", line 194, in __rpc__
        response = self._exec_jsonrpc(name, *args, **kwargs)
      File "/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/.venv/lib/python3.9/site-packages/ansible/module_utils/connection.py", line 155, in _exec_jsonrpc
        out = self.send(data)
      File "/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/.venv/lib/python3.9/site-packages/ansible/module_utils/connection.py", line 214, in send
        raise ConnectionError(
    ansible.module_utils.connection.ConnectionError: unable to connect to socket /Users/rahulpurohit/.ansible/pc/0f3c863d2b. See the socket path issue category in Network Debug and Troubleshooting Guide

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/.venv/bin/ansible-connection", line 8, in <module>
        sys.exit(main())
      File "/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/.venv/lib/python3.9/site-packages/ansible/cli/scripts/ansible_connection_cli_stub.py", line 318, in main
        raise ConnectionError('Unable to decode JSON from response set_options. See the debug log for more information.')
    ansible.module_utils.connection.ConnectionError: Unable to decode JSON from response set_options. See the debug log for more information.

TASK [arista.avd.eos_designs : Verify Requirements] ********************************************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:19:50 -0400 (0:00:01.958)       0:00:03.906 ******
AVD version 4.10.2
Use -v for details.
ok: [QNFDS003-E285-CS01 -> localhost]

TASK [arista.avd.eos_designs : Create required output directories if not present] **************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:19:50 -0400 (0:00:00.179)       0:00:04.085 ******
ok: [QNFDS003-E285-CS01 -> localhost] => (item=/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/inventory/..//intended/structured_configs)
ok: [QNFDS003-E285-CS01 -> localhost] => (item=/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/inventory/..//documentation/fabric)

TASK [arista.avd.eos_designs : Set eos_designs facts] ******************************************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:19:52 -0400 (0:00:01.947)       0:00:06.033 ******
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[0].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[1].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[2].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[3].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[4].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[5].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[6].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[7].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[0].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[1].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[2].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[3].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[4].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[5].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[6].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[7].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
ok: [QNFDS003-E285-CS01]
/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(

TASK [arista.avd.eos_designs : Generate device configuration in structured format] *************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:19:55 -0400 (0:00:02.925)       0:00:08.958 ******
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[0].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[1].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[2].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[3].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[4].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[5].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[6].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[7].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
ok: [QNFDS003-E285-CS01 -> localhost]

TASK [arista.avd.eos_designs : Remove avd_switch_facts] ****************************************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:19:57 -0400 (0:00:01.948)       0:00:10.907 ******
ok: [QNFDS003-E285-CS01]

TASK [iosxe_cli_config_gen : Create required output directories if not present] ****************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:19:58 -0400 (0:00:01.513)       0:00:12.421 ******
ok: [QNFDS003-E285-CS01 -> localhost] => (item=/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/inventory/..//intended/structured_configs)
ok: [QNFDS003-E285-CS01 -> localhost] => (item=/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/inventory/..//intended/QN/QNFDS003-E285)

TASK [iosxe_cli_config_gen : Include device intended structure configuration variables] ********************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:20:00 -0400 (0:00:01.435)       0:00:13.856 ******
ok: [QNFDS003-E285-CS01 -> localhost]

TASK [iosxe_cli_config_gen : Generate iosxe intended configuration] ****************************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:20:00 -0400 (0:00:00.270)       0:00:14.126 ******
changed: [QNFDS003-E285-CS01 -> localhost]

PLAY RECAP *************************************************************************************************************************************************************************************************************************************************************************************************************************************************************
QNFDS003-E285-CS01         : ok=10   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
QNFDS012-E294-CS01         : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0

Friday 20 September 2024  17:20:02 -0400 (0:00:01.959)       0:00:16.086 ******
===============================================================================
arista.avd.eos_designs : Set eos_designs facts ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 2.93s
iosxe_cli_config_gen : Generate iosxe intended configuration ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.96s
Set custom output directory ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.96s
arista.avd.eos_designs : Generate device configuration in structured format ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.95s
arista.avd.eos_designs : Create required output directories if not present -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.95s
Extract vars from hostname to be used in custom filters --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.72s
arista.avd.eos_designs : Remove avd_switch_facts ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.51s
iosxe_cli_config_gen : Create required output directories if not present ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.44s
iosxe_cli_config_gen : Include device intended structure configuration variables -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 0.27s
arista.avd.eos_designs : Verify Requirements -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 0.18s
make: *** [build-cisco] Error 2
(.venv) rahulpurohit@Rahuls-MacBook-Pro firehouse-fdny-github %
(.venv) rahulpurohit@Rahuls-MacBook-Pro firehouse-fdny-github %
(.venv) rahulpurohit@Rahuls-MacBook-Pro firehouse-fdny-github %
(.venv) rahulpurohit@Rahuls-MacBook-Pro firehouse-fdny-github % make build-cisco
ansible-playbook playbooks/build-cisco.yml --skip-tags documentation
/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/.venv/lib/python3.9/site-packages/paramiko/pkey.py:100: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from this module in 48.0.0.
  "cipher": algorithms.TripleDES,
/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/.venv/lib/python3.9/site-packages/paramiko/transport.py:259: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from this module in 48.0.0.
  "class": algorithms.TripleDES,
all /Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/inventory

PLAY [Run Cisco AVD] ***************************************************************************************************************************************************************************************************************************************************************************************************************************************************

TASK [Extract vars from hostname to be used in custom filters] *********************************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:21:38 -0400 (0:00:00.193)       0:00:00.193 ******
[WARNING]: ansible-pylibssh not installed, falling back to paramiko
[WARNING]: ansible-pylibssh not installed, falling back to paramiko
ok: [QNFDS003-E285-CS01]
ok: [QNFDS012-E294-CS01]

TASK [Set custom output directory] *************************************************************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:21:39 -0400 (0:00:01.504)       0:00:01.698 ******
ok: [QNFDS012-E294-CS01]
ok: [QNFDS003-E285-CS01]

TASK [arista.avd.eos_designs : Verify Requirements] ********************************************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:21:41 -0400 (0:00:01.388)       0:00:03.086 ******
AVD version 4.10.2
Use -v for details.
ok: [QNFDS012-E294-CS01 -> localhost]

TASK [arista.avd.eos_designs : Create required output directories if not present] **************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:21:41 -0400 (0:00:00.154)       0:00:03.241 ******
ok: [QNFDS012-E294-CS01 -> localhost] => (item=/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/inventory/..//intended/structured_configs)
ok: [QNFDS012-E294-CS01 -> localhost] => (item=/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/inventory/..//documentation/fabric)

TASK [arista.avd.eos_designs : Set eos_designs facts] ******************************************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:21:42 -0400 (0:00:01.502)       0:00:04.744 ******
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[0].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[1].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[2].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[3].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[4].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[5].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[6].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[7].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[0].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[1].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[2].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[3].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[4].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[5].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[6].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[7].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
ok: [QNFDS012-E294-CS01]
/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(

TASK [arista.avd.eos_designs : Generate device configuration in structured format] *************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:21:45 -0400 (0:00:02.427)       0:00:07.172 ******
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[0].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[1].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[2].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[3].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[4].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[5].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[6].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[0].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS012-E294-CS01]: 'Validation Error: tenants[0].vrfs[7].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[1].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[2].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[3].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[4].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[5].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[6].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
[WARNING]: [QNFDS003-E285-CS01]: 'Validation Error: tenants[0].vrfs[7].structured_config.vrfs[0]': Unexpected key(s) 'rd' found in dict.
ok: [QNFDS003-E285-CS01 -> localhost]
ok: [QNFDS012-E294-CS01 -> localhost]

TASK [arista.avd.eos_designs : Remove avd_switch_facts] ****************************************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:21:47 -0400 (0:00:01.972)       0:00:09.145 ******
ok: [QNFDS012-E294-CS01]

TASK [iosxe_cli_config_gen : Create required output directories if not present] ****************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:21:48 -0400 (0:00:01.388)       0:00:10.534 ******
ok: [QNFDS012-E294-CS01 -> localhost] => (item=/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/inventory/..//intended/structured_configs)
ok: [QNFDS012-E294-CS01 -> localhost] => (item=/Users/rahulpurohit/FDNY-local/fdny-fh/firehouse-fdny-github/inventory/..//intended/QN/QNFDS012-E294)

TASK [iosxe_cli_config_gen : Include device intended structure configuration variables] ********************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:21:49 -0400 (0:00:01.101)       0:00:11.635 ******
ok: [QNFDS012-E294-CS01 -> localhost]
ok: [QNFDS003-E285-CS01 -> localhost]

TASK [iosxe_cli_config_gen : Generate iosxe intended configuration] ****************************************************************************************************************************************************************************************************************************************************************************************************
Friday 20 September 2024  17:21:50 -0400 (0:00:00.249)       0:00:11.885 ******
ok: [QNFDS003-E285-CS01 -> localhost]
changed: [QNFDS012-E294-CS01 -> localhost]

PLAY RECAP *************************************************************************************************************************************************************************************************************************************************************************************************************************************************************
QNFDS003-E285-CS01         : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
QNFDS012-E294-CS01         : ok=10   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

Friday 20 September 2024  17:21:51 -0400 (0:00:01.829)       0:00:13.715 ******
===============================================================================
arista.avd.eos_designs : Set eos_designs facts ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 2.43s
arista.avd.eos_designs : Generate device configuration in structured format ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.97s
iosxe_cli_config_gen : Generate iosxe intended configuration ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.83s
Extract vars from hostname to be used in custom filters --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.50s
arista.avd.eos_designs : Create required output directories if not present -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.50s
arista.avd.eos_designs : Remove avd_switch_facts ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.39s
Set custom output directory ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.39s
iosxe_cli_config_gen : Create required output directories if not present ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1.10s
iosxe_cli_config_gen : Include device intended structure configuration variables -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 0.25s
arista.avd.eos_designs : Verify Requirements -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 0.15s
(.venv) rahulpurohit@Rahuls-MacBook-Pro firehouse-fdny-github %
```
