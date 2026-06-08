#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   LIGHTNING UBC                          ║
║   Pagamentos instantâneos off-chain      ║
╚══════════════════════════════════════════╝
"""
import json, os, secrets, hashlib
from datetime import datetime

class LightningUBC:
    def __init__(self):
        self.canais = {}
        self.transacoes = []
        self.carregar()
    
    def carregar(self):
        if os.path.exists('lightning.json'):
            with open('lightning.json') as f:
                d = json.load(f)
                self.canais = d.get('canais', {})
                self.transacoes = d.get('transacoes', [])
    
    def salvar(self):
        with open('lightning.json', 'w') as f:
            json.dump({'canais': self.canais, 'transacoes': self.transacoes}, f, indent=2)
    
    def abrir_canal(self, parte1, parte2, valor):
        canal_id = secrets.token_hex(16)
        self.canais[canal_id] = {"partes": [parte1, parte2], "capacidade": valor, "saldo_1": valor, "saldo_2": 0, "status": "aberto"}
        self.salvar()
        return {"ok": True, "canal_id": canal_id, "capacidade": valor}
    
    def pagar(self, canal_id, pagador, valor):
        if canal_id not in self.canais: return {"erro": "Canal não encontrado"}
        c = self.canais[canal_id]
        if c['partes'][0] == pagador and c['saldo_1'] >= valor:
            c['saldo_1'] -= valor
            c['saldo_2'] += valor
            self.transacoes.append({"canal": canal_id, "valor": valor, "hash": hashlib.sha256(f"{valor}{datetime.now()}".encode()).hexdigest()[:16], "tipo": "lightning_ubc"})
            self.salvar()
            return {"ok": True, "instantaneo": True, "taxa": 0}
        return {"erro": "Saldo insuficiente"}

print("✅ Lightning UBC pronto")
