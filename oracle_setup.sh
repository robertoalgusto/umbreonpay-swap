#!/bin/bash
# ╔══════════════════════════════════════════╗
# ║   SERVIDOR ORACLE — SETUP AUTOMÁTICO    ║
# ║   Always Free Tier — 24/7               ║
# ╚══════════════════════════════════════════╝

echo "🖥️ Configurando servidor Oracle..."

# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python e dependências
sudo apt install python3 python3-pip nginx git -y

# Clonar APIs da UmbreonPay
cd ~
git clone https://github.com/robertoalgusto/umbreonpay-api.git
cd umbreonpay-api
pip3 install -r requirements.txt

# Configurar serviço systemd (24/7)
sudo cat > /etc/systemd/system/umbreonpay.service << 'SERVICE'
[Unit]
Description=UmbreonPay API
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/umbreonpay-api
ExecStart=/usr/bin/python3 app.py
Restart=always

[Install]
WantedBy=multi-user.target
SERVICE

# Iniciar serviço
sudo systemctl enable umbreonpay
sudo systemctl start umbreonpay

echo "✅ Servidor Oracle configurado!"
echo "🔗 API rodando em: http://$(curl -s ifconfig.me):8080"
