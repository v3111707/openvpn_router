#!/usr/bin/env python3

import socket
import os

routes_file = 'routes'
sites_file = 'blocked_sites'
ip_list = []


def site_to_ip(url):
    ip_list = []
    try:
        ais = socket.getaddrinfo(host=url, port=0, family=socket.AF_INET)
    except:
        print(url)
    else:
        for result in ais:
            ip_list.append(result[-1][0])
    url = 'www.' + url
    try:
        ais = socket.getaddrinfo(host=url, port=0, family=socket.AF_INET)
    except:
        print(url)
    else:
        for result in ais:
            ip_list.append(result[-1][0])
    return ip_list

with open(sites_file) as f:
    for url in f.read().splitlines():
        ip_list.extend(site_to_ip(url))



ip_list = list(set(ip_list))

f = open(routes_file, 'w')

for ip in ip_list:
    f.write(f'route {ip} 255.255.255.255 \n')
f.close()

#os.system("/etc/init.d/openvpn restart")

