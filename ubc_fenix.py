#!/usr/bin/env python3
"""UBC Fénix — Dinheiro com timeout de autodestruição"""
import json, os
from datetime import datetime, timedelta

class UBCFenix:
    def __init__(self):
        self.ativos = {}
        self.carregar()
    def carregar(self):
        if os.path.exists('fenix.json'):
            with open('fenix.json') as f: self.ativos = json.load(f)
    def salvar(self):
        with open('fenix.json', 'w') as f: json.dump(self.ativos, f, indent=2)
    def criar(self, carteira, valor, dias=30):
        tid = secrets.token_hex(8)
        self.ativos[tid] = {"carteira": carteira, "valor": valor, "expira": (datetime.now() + timedelta(days=dias)).isoformat(), "status": "ativo"}
        self.salvar()
        return {"ok": True, "id": tid, "expira_em": f"{dias} dias"}
    def verificar(self):
        queimados = 0
        for tid, a in list(self.ativos.items()):
            if a['status'] == 'ativo' and datetime.now().isoformat() > a['expira']:
                a['status'] = 'queimado'
                queimados += a['valor']
        self.salvar()
        return {"ok": True, "queimados": queimados, "mensagem": "UBC queimado voltou ao lastro"}
print("✅ UBC Fénix pronto")
