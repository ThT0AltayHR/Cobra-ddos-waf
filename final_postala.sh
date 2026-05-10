#!/bin/bash

# Renkler
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${CYAN}[*] Cobra GitHub Operasyonu Başlatılıyor...${NC}"

# Kullanıcı ve Repo Bilgileri (Güncellendi)
TOKEN="Ghp_ZwNxo6jwMAu3svo1TK9DVne8j2GxlM3OvBDp"
REPO_URL="github.com/ThT0AltayHR/Cobra-ddos-waf.git"
USER_NAME="ThT0AltayHR"
USER_EMAIL="balinmuhammed722@gmail.com"

# Git Konfigürasyonu
git config --global user.name "$USER_NAME"
git config --global user.email "$USER_EMAIL"
git config --global --add safe.directory $(pwd)

# Repo Hazırlık
if [ ! -d ".git" ]; then
    git init
    echo -e "${GREEN}[+] Yeni yerel depo oluşturuldu.${NC}"
fi

# Dosyaları Ekle ve Commit At
git add .
git commit -m "Cobra v1.0 - Anka Red Team | Persistence & Hunter Mode"

# Uzak Repo Bağlantısı (Token ile Yetkilendirme)
git remote remove origin 2>/dev/null
git remote add origin "https://$USER_NAME:$TOKEN@$REPO_URL"

# FORCE PUSH - Meydan Okuma
echo -e "${CYAN}[*] Cobra GitHub'a fırlatılıyor (Force Mode)...${NC}"
git branch -M main
git push -u origin main --force

if [ $? -eq 0 ]; then
    echo -e "${GREEN}--------------------------------------------------${NC}"
    echo -e "${GREEN}[TAMAMLANDI] Cobra artık yayında, dünya görsün!${NC}"
    echo -e "${GREEN}Repo: https://$REPO_URL${NC}"
    echo -e "${GREEN}--------------------------------------------------${NC}"
else
    echo -e "${RED}[!] Hata: Bağlantıyı veya Token yetkilerini kontrol et.${NC}"
fi
