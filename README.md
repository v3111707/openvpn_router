# openvpn

```bash
opkg update
opkg install python3-light python3-pip
opkg install git-http
opkg install openvpn-openssl openvpn-easy-rsa luci-i18n-openvpn-en rsync
cd /etc/openvpn/
git clone https://github.com/v3111707/openvpn_router.git .
#see nl_nordvpn.auth in enpass


# Click on Network in the top bar and then on Firewall to open the firewall configuration page.

# Click on the Edit button of the wan (red) zone in the Zones list at the bottom of the page.

# Click on the Advanced Settings tab and select the tunX interface (tun0 in the screenshot, which is the most likely if you have a single OpenVPN client/server running)


service openvpn enable
service openvpn start

```
