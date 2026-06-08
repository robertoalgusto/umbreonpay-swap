#!/usr/bin/env python3
"""UBC RENT — Alugue seu saldo para traders"""
import json, os
from datetime import datetime

class UBCRent:
    RENTABILIDADE_DIARIA = 0.001  # 0.1% ao dia
    def __init__(self):
        self.contratos = {}
        self.carregar()
    def carregar(self):
        if os.path.exists('rent.json'):
            with open('rent.json') as f: self.contratos = json.load(f)
    def salvar(self):
        with open('rent.json', 'w') as f: json.dump(self.contratos, f, indent=2)
    def alugar(self, proprietario, valor, dias=1):
        rendimento = round(valor * self.RENTABILIDADE_DIARIA * dias, 4)
        self.contratos[proprietario] = {"valor": valor, "dias": dias, "rendimento": rendimento, "inicio": datetime.now().isoformat()}
        self.salvar()
        return {"ok": True, "rendimento": rendimento, "mensagem": f"Seu dinheiro trabalha enquanto você dorme. +{rendimento} UBC em {dias} dia(s)"}
    def resgatar(self, proprietario):
        if proprietario not in self.contratos: return {"erro": "Sem contratos ativos"}
        c = self.contratos[proprietario]
        total = c['valor'] + c['rendimento']
        del self.contratos[proprietario]
        self.salvar()
        return {"ok": True, "valor_original": c['valor'], "rendimento": c['rendimento'], "total": total}
print("✅ UBC RENT pronto")
