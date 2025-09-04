import xml.etree.ElementTree as ET
import re

tree = ET.parse('scan_results.xml')
root = tree.getroot()

ip_map = {}  # Map real IPs to fake ones
mac_map = {}  # Similarly for MACs
hostname_map = {}
fake_ip_base = '10.0.0.'
fake_mac_base = '00:00:00:00:00:'
counter = 1

for host in root.findall('host'):
    for addr in host.findall('address'):
        if addr.get('addrtype') == 'ipv4':
            real_ip = addr.get('addr')
            if real_ip not in ip_map:
                ip_map[real_ip] = fake_ip_base + str(counter)
                counter += 1
            addr.set('addr', ip_map[real_ip])
        elif addr.get('addrtype') == 'mac':
            real_mac = addr.get('addr')
            if real_mac not in mac_map:
                mac_map[real_mac] = fake_mac_base + format(counter, '02x')
                counter += 1
            addr.set('addr', mac_map[real_mac])
            if addr.get('vendor'):
                addr.set('vendor', 'FakeVendor-' + str(counter))

    for hostname in host.findall('hostnames/hostname'):
        real_name = hostname.get('name')
        if real_name not in hostname_map:
            hostname_map[real_name] = 'Device-' + str(counter)
            counter += 1
        hostname.set('name', hostname_map[real_name])

tree.write('sanitized_scan.xml')
