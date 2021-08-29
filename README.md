# openvpn

```bash
opkg update
opkg install python3-light, python3-pip
opkg install git-http
opkg install openvpn-openssl openvpn-easy-rsa luci-i18n-openvpn-en rsync
cd /etc/openvpn/
git clone https://github.com/v3111707/openvpn_router.git .
#see nl_nordvpn.auth in enpass
service openvpn enable
service openvpn start
```