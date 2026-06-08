#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   UBC SAVINGS — POUPANÇA                 ║
║   Rendimento automático                  ║
╚══════════════════════════════════════════╝
"""
import json, os
from datetime import datetime, timedelta

class UBCSavings:
    RENDIMENTO_MENSAL = 0.05  # 5% ao mês
    
    def __init__(self):
        self.contas = {}
        self.carregar()
    
    def carregar(self):
        if os.path.exists('savings.json'):
            with open('savings.json') as f:
                self.contas = json.load(f)
    
    def salvar(self):
        with open('savings.json', 'w') as f:
            json.dump(self.contas, f, indent=2)
    
    def depositar(self, carteira, valor_ubc):
        """Deposita UBC na poupança"""
        if carteira not in self.contas:
            self.contas[carteira] = {"saldo": 0, "rendimento_total": 0, "ultimo_rendimento": datetime.now().isoformat()}
        self.contas[carteira]['saldo'] += valor_ubc
        self.salvar()
        return {"ok": True, "novo_saldo": self.contas[carteira]['saldo']}
    
    def calcular_rendimento(self, carteira):
        """Calcula rendimento acumulado"""
        if carteira not in self.contas: return {"erro": "Conta não encontrada"}
        c = self.contas[carteira]
        dias = (datetime.now() - datetime.fromisoformat(c['ultimo_rendimento'])).days
        if dias < 30: return {"rendimento": 0, "dias": dias, "proximo_rendimento": 30 - dias}
        rendimento = round(c['saldo'] * self.RENDIMENTO_MENSAL, 4)
        c['saldo'] += rendimento
        c['rendimento_total'] += rendimento
        c['ultimo_rendimento'] = datetime.now().isoformat()
        self.salvar()
        return {"ok": True, "rendimento": rendimento, "novo_saldo": c['saldo']}

print("✅ UBC Savings pronto")
