#!/usr/bin/env python3
"""UBC Shield — Seguro de transação 0.1%"""
import json, os

class UBCShield:
    TAXA = 0.001
    def __init__(self):
        self.fundo = 0
        self.segurados = {}
        self.carregar()
    def carregar(self):
        if os.path.exists('shield.json'):
            with open('shield.json') as f: d = json.load(f); self.fundo = d.get('fundo', 0); self.segurados = d.get('segurados', {})
    def salvar(self):
        with open('shield.json', 'w') as f: json.dump({'fundo': self.fundo, 'segurados': self.segurados}, f, indent=2)
    def ativar(self, carteira):
        self.segurados[carteira] = {"ativo": True, "transacoes": 0}
        self.salvar()
        return {"ok": True, "mensagem": "Shield ativado. 0.1% extra por transação. Cobertura contra falhas."}
    def cobrir(self, carteira, valor):
        if carteira in self.segurados and self.fundo >= valor:
            self.fundo -= valor
            self.salvar()
            return {"ok": True, "coberto": valor}
        return {"erro": "Cobertura negada"}
print("✅ UBC Shield pronto")
