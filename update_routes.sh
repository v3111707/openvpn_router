#!/bin/sh
git pull
python3 routes_generator.py
/etc/init.d/openvpn restart
