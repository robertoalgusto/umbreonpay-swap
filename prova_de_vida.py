#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   PROVA DE VIDA (UBC ALIVE)              ║
║   Confirmação periódica de existência    ║
╚══════════════════════════════════════════╝
"""
import json, os, secrets
from datetime import datetime, timedelta

class ProvaDeVida:
    INTERVALO_MESES = 6
    
    def __init__(self):
        self.usuarios = {}
        self.carregar()
    
    def carregar(self):
        if os.path.exists('alive.json'):
            with open('alive.json') as f:
                self.usuarios = json.load(f)
    
    def salvar(self):
        with open('alive.json', 'w') as f:
            json.dump(self.usuarios, f, indent=2)
    
    def registrar(self, carteira):
        self.usuarios[carteira] = {"ultima_prova": datetime.now().isoformat(), "status": "vivo", "codigo_verificacao": secrets.token_hex(4)}
        self.salvar()
        return {"ok": True, "codigo": self.usuarios[carteira]['codigo_verificacao']}
    
    def verificar(self, carteira, codigo):
        if carteira not in self.usuarios: return {"erro": "Usuário não registrado"}
        u = self.usuarios[carteira]
        if codigo != u['codigo_verificacao']: return {"erro": "Código inválido"}
        u['ultima_prova'] = datetime.now().isoformat()
        u['codigo_verificacao'] = secrets.token_hex(4)
        self.salvar()
        return {"ok": True, "status": "✅ Vivo", "proxima": (datetime.now() + timedelta(days=self.INTERVALO_MESES*30)).strftime("%d/%m/%Y")}
    
    def verificar_inatividade(self):
        alertas = []
        for cart, u in self.usuarios.items():
            if u['status'] == 'vivo':
                ultima = datetime.fromisoformat(u['ultima_prova'])
                if datetime.now() - ultima > timedelta(days=self.INTERVALO_MESES * 30):
                    u['status'] = 'alerta'
                    alertas.append({"carteira": cart, "dias_inativo": (datetime.now() - ultima).days})
        self.salvar()
        return {"ok": True, "alertas": alertas}

print("✅ Prova de Vida pronta")
