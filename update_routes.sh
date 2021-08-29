#!/bin/sh
git pull
python3 routes_generator.py
service openvpn restart
