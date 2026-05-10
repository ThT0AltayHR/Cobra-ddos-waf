import os
from scapy.all import sniff, IP, TCP, UDP
from collections import defaultdict
import time
from core.strike import ReverseStrike

class CobraDetector:
    def __init__(self, protected_ip):
        self.protected_ip = protected_ip
        self.packet_counts = defaultdict(int)
        self.first_seen = defaultdict(time.time)
        self.threshold = 150 # Saniyede 150 paketi aşarsa DDoS say
        self.blocked_ips = set()
        self.striker = ReverseStrike()

    def block_ip(self, attacker_ip):
        if attacker_ip not in self.blocked_ips:
            print(f"[\033[1;33m*\033[0m] KALKAN AKTİF: {attacker_ip} bloklanıyor...")
            # Iptables ile paketi tamamen drop et
            os.system(f"iptables -A INPUT -s {attacker_ip} -j DROP")
            self.blocked_ips.add(attacker_ip)
            
            # Savunma bitti, taarruz başlasın
            self.striker.launch(attacker_ip)

    def process_packet(self, pkt):
        if IP in pkt:
            src_ip = pkt[IP].src
            dst_ip = pkt[IP].dst

            # Eğer paket korunan IP'ye geliyorsa analiz et
            if dst_ip == self.protected_ip or self.protected_ip == "0.0.0.0":
                current_time = time.time()
                self.packet_counts[src_ip] += 1
                
                # Zaman farkını hesapla
                time_diff = current_time - self.first_seen[src_ip]
                
                if time_diff >= 1.0:
                    pps = self.packet_counts[src_ip] / time_diff
                    if pps > self.threshold and src_ip not in self.blocked_ips:
                        self.block_ip(src_ip)
                    
                    # Sayacı sıfırla
                    self.packet_counts[src_ip] = 0
                    self.first_seen[src_ip] = current_time

    def start_sniffing(self):
        print(f"[\033[1;32m+\033[0m] Cobra Ağı Dinliyor... (Korunan IP: {self.protected_ip})")
        # Tüm arayüzlerde sadece gelen trafiği dinle
        sniff(filter="ip", prn=self.process_packet, store=False)
