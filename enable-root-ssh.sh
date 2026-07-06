#!/bin/bash

set -e

CONFIG="/etc/ssh/sshd_config"

echo "[+] Setze PermitRootLogin..."

if grep -q "^PermitRootLogin" $CONFIG; then
    sed -i 's/^PermitRootLogin.*/PermitRootLogin yes/' $CONFIG
else
    echo "PermitRootLogin yes" >> $CONFIG
fi

echo "[+] Restart SSH..."
systemctl restart ssh || systemctl restart sshd

echo "[✔] Fertig. Root Login via SSH ist jetzt an."
