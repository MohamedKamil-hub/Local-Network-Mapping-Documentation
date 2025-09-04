import xml.etree.ElementTree as ET

tree = ET.parse('sanitized_scan.xml')
root = tree.getroot()

dot_content = 'digraph Network {\n'
dot_content += '    node [shape=box];\n'

router_ip = None  # Assume lowest IP is router, e.g., .1
devices = []

for host in root.findall('host'):
    ip = None
    mac = None
    hostname = 'Unknown'
    vendor = 'Unknown'

    for addr in host.findall('address'):
        if addr.get('addrtype') == 'ipv4':
            ip = addr.get('addr')
        elif addr.get('addrtype') == 'mac':
            mac = addr.get('addr')
            vendor = addr.get('vendor', 'Unknown')

    for hname in host.findall('hostnames/hostname'):
        hostname = hname.get('name')

    label = f"{hostname}\\nIP: {ip}\\nMAC: {mac}\\nVendor: {vendor}"
    dot_content += f'    "{ip}" [label="{label}"];\n'
    devices.append(ip)

    if not router_ip or (ip and int(ip.split('.')[-1]) < int(router_ip.split('.')[-1])):
        router_ip = ip

# Connect all to router (simple topology)
for device_ip in devices:
    if device_ip != router_ip:
        dot_content += f'    "{router_ip}" -> "{device_ip}";\n'

dot_content += '}\n'

with open('network_topology.dot', 'w') as f:
    f.write(dot_content)
