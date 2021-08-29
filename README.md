# openvpn

```bash
opkg update
opkg install python3-light
opkg install git
opkg install openvpn-openssl openvpn-easy-rsa luci-i18n-openvpn-en rsync
cd /etc/openvpn/
git pull git@github.com:v3111707/openvpn.git

service openvpn enable
service openvpn start
```