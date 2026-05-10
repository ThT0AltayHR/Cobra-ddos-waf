#!/bin/bash
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

# Bilgiler (KONTROL ET: Token'da boşluk olmasın)
TOKEN="Ghp_ZwNxo6jwMAu3svo1TK9DVne8j2GxlM3OvBDp"
USER="ThT0AltayHR"
REPO="Cobra-ddos-waf.git"

echo -e "${GREEN}[*] Kimlik doğrulama onarılıyor...${NC}"

# Remote URL'yi en güvenli formatta ekle
git remote add origin "https://${TOKEN}@github.com/${USER}/${REPO}"

echo -e "${GREEN}[*] Force Push başlatılıyor...${NC}"
git branch -M main
git push -u origin main --force

if [ $? -eq 0 ]; then
    echo -e "${GREEN}[KUSURSUZ] Cobra başarıyla Github'a sızdı!${NC}"
else
    echo -e "${RED}[!] Hata devam ediyor. Token yetkilerini (repo & workflow) kontrol et.${NC}"
fi
