adduser anil
usermod -aG sudo anil
ufw app list
ufw allow OpenSSH
ufw enable
ufw status