import os
import sys
import socket
from core.detector import CobraDetector

def clear_screen():
    os.system('clear')

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def daemonize():
    """Terminal kapansa bile Cobra'nın yaşamasını sağlar."""
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as e:
        sys.stderr.write(f"Fork #1 koptu: {e}\n")
        sys.exit(1)

    os.setsid()

    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as e:
        sys.stderr.write(f"Fork #2 koptu: {e}\n")
        sys.exit(1)

def banner():
    print("""\033[1;32m
     ____ ___  ____  ____      _    
    / ___/ _ \| __ )|  _ \    / \   
   | |  | | | |  _ \| |_) |  / _ \  
   | |__| |_| | |_) |  _ <  / ___ \ 
    \____\___/|____/|_| \_\/_/   \_\
    
    [ Anka Red Team - Vatan Nöbeti ]
\033[0m""")

def main():
    if os.geteuid() != 0:
        print("[\033[1;31m!\033[0m] Cobra'nın çalışması için ROOT (tsu/sudo) yetkisi gereklidir.")
        sys.exit()

    clear_screen()
    banner()
    
    print("1) Otomatik Mod (Yerel IP'yi Koru)")
    print("2) Manuel Mod (Spesifik IP Gir)")
    
    choice = input("Seçiminiz (1/2): ")
    
    if choice == '1':
        target_ip = get_local_ip()
    elif choice == '2':
        target_ip = input("Korunacak IP Adresini Girin: ")
    else:
        print("Hatalı seçim.")
        sys.exit()

    print(f"[\033[1;32m+\033[0m] Cobra Başlatılıyor. Terminali kapatsanız bile arka planda çalışmaya devam edecek.")
    
    # Arka plana alma (Daemon) işlemini onayla
    daemonize()
    
    # Cobra'yı ateşle
    detector = CobraDetector(target_ip)
    detector.start_sniffing()

if __name__ == "__main__":
    main()
