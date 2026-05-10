#!/bin/bash
echo "[*] Cobra bağımlılıkları kuruluyor..."
pkg update -y
pkg install python root-repo -y
pkg install iptables scapy tsu -y
pip install scapy
echo "[+] Kurulum tamamlandı. Başlatmak için: sudo python3 cobra.py"
