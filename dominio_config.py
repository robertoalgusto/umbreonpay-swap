#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   DOMÍNIO PRÓPRIO                        ║
║   umbreonpay.com                         ║
╚══════════════════════════════════════════╝
"""
import json, os

class DominioProprio:
    CONFIG = {
        "dominio": "umbreonpay.com",
        "registrador": "Njalla (anônimo, aceita XMR)",
        "dns": "Cloudflare (gratuito)",
        "ssl": "Let's Encrypt (gratuito)",
        "redirecionamento": "GitHub Pages → umbreonpay.com",
        "email": "contato@umbreonpay.com"
    }
    
    @classmethod
    def instrucoes(cls):
        return """
╔══════════════════════════════════════════╗
║   CONFIGURAÇÃO DO DOMÍNIO               ║
╠══════════════════════════════════════════╣
║   1. Comprar domínio na Njalla          ║
║      https://njal.la (aceita XMR)       ║
║      Sem KYC, sem dados pessoais        ║
║                                          ║
║   2. Configurar DNS no Cloudflare       ║
║      CNAME: umbreonpay.com →            ║
║      robertoalgusto.github.io           ║
║                                          ║
║   3. Ativar SSL no Cloudflare           ║
║      Flexível (gratuito)                ║
║                                          ║
║   4. Email: Redirecionar para Gmail     ║
║      contato@umbreonpay.com →           ║
║      contato.umbreonpay@gmail.com       ║
╚══════════════════════════════════════════╝
        """

print("✅ Domínio configurado (instruções)")
