#!/usr/bin/env python3
"""UBC FAMILY — Democracia financeira familiar"""
import json, os

class UBCFamily:
    def __init__(self):
        self.carteiras = {}
        self.carregar()
    def carregar(self):
        if os.path.exists('family.json'):
            with open('family.json') as f: self.carteiras = json.load(f)
    def salvar(self):
        with open('family.json', 'w') as f: json.dump(self.carteiras, f, indent=2)
    def criar(self, membros, limite_aprovacao=500):
        self.carteiras['familia'] = {"membros": membros, "saldo": 0, "limite_aprovacao": limite_aprovacao, "aprovacoes_necessarias": max(1, len(membros) // 2)}
        self.salvar()
        return {"ok": True, "membros": len(membros), "aprovacoes_necessarias": self.carteiras['familia']['aprovacoes_necessarias']}
    def solicitar_saque(self, membro, valor):
        if valor > self.carteiras['familia']['limite_aprovacao']:
            return {"erro": f"Valor acima de R$ {self.carteiras['familia']['limite_aprovacao']} requer {self.carteiras['familia']['aprovacoes_necessarias']} aprovações"}
        return {"ok": True, "aprovado": True}
print("✅ UBC FAMILY pronto")
