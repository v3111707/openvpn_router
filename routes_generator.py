#!/usr/bin/env python3

import socket
import os

routes_file = '/etc/openvpn/routes'
routes_file = 'routes'

banned_sites = ['primaries.by',
                'udf.by',
                'masheka.by',
                'progomel.by',
                'pyx.by',
                'tip.by',
                'virtualbrest.by',
                'vkurier.by',
                '015.by',
                'tsepkalo.info',
                'tsepkalo.com',
                'honestby.org',
                'babariko.vision',
                'agitka2020.com',
                'euroradio.fm',
                'opg.ucoz.net',
                'narodny-opros.info',
                'statkevich.org',
                'belarus.regnum.ru',
                'belsat.eu',
                'eurobelarus.info',
                'gazetaby.com',
                'mfront.net',
                'spring96.org',
                'ucpb.org',
                'praca-by.info',
                'svaboda.org',
                'svaboda2.net',
                'zapraudu.info',
                'bchd.info',
                'belarusinfocus.info',
                'belprauda.org',
                'elections2020.spring96.org',
                'flagshtok.info',
                'hramada.org',
                'mspring.online',
                'news.vitebsk.cc',
                'politnavigator.net',
                'vitebskspring.org',
                'vot-tak.tv',
                'moyby.com',
                'the-village.me',
                'zona.media',
                'by.tribuna.com',
                'Afn.by',
                'belarus2020.org',
                'zubr.in',
                'startmail.com',
                'tutanota.com',
                'cock.li',
                'protonmai1.com',
                'psiphon.ca',
                'txti.es',
                'liveu.tv',
                'surfshark.com',
                'zenmate.com',
                'safervpn.com',
                'mssg.me',
                'is.gd',
                'tgproxy.me',
                'dmp2.org',
                'proxy-gram.tk',
                'zharov-lox.telegramproxy.me',
                'catalog-telegram.ru',
                'telegram-socks.tk',
                'prx.nmja',
                'proxygram.org',
                'tlgrm.mnja',
                'telegramproxy.online',
                'rusproxy.telegramproxy.me',
                'tginfo.yadda.club',
                'telegram.veesecurity.com',
                'vamtlgrm.com',
                'kyky.org',
                'naviny.by',
		'naviny.online',
		'naviny.media'
]
ip_list = []

for host in banned_sites:
    try:
        ais = socket.getaddrinfo(host=host, port=0, family=socket.AF_INET)
    except:
        print(host)
    else:
        for result in ais:
            ip_list.append(result[-1][0])
    host = 'www.' + host
    try:
        ais = socket.getaddrinfo(host=host, port=0, family=socket.AF_INET)
    except:
        print(host)
    else:
        for result in ais:
            ip_list.append(result[-1][0])


ip_list = list(set(ip_list))

f = open(routes_file, 'w')

for ip in ip_list:
    f.write(f'route {ip} 255.255.255.255 \n')
f.close()

os.system("/etc/init.d/openvpn restart")


