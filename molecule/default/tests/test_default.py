import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    hosts_file = host.file('/etc/hosts')

    assert hosts_file.exists
    assert hosts_file.user == 'root'
    assert hosts_file.group == 'root'


def test_azurite_process_running(host):
    azurite = [
        process for process in
        host.process.filter(user="www-data", comm="node")
        if process.args.find('azurite') != -1
    ]

    assert len(azurite) > 0
