#!/usr/bin/env python3
"""UBC LIVING WILL — Herança parcelada em vida"""
import json, os

class UBCLivingWill:
    PCT_MENSAL = 5
    def __init__(self):
        self.herancas = {}
        self.carregar()
    def carregar(self):
        if os.path.exists('living.json'):
            with open('living.json') as f: self.herancas = json.load(f)
    def salvar(self):
        with open('living.json', 'w') as f: json.dump(self.herancas, f, indent=2)
    def configurar(self, origem, herdeiro, valor_total):
        self.herancas[origem] = {"herdeiro": herdeiro, "total": valor_total, "liberado": 0, "mensal": round(valor_total * self.PCT_MENSAL / 100, 2)}
        self.salvar()
        return {"ok": True, "mensagem": f"{herdeiro} receberá {self.PCT_MENSAL}% ao mês. Sem inventário. Sem imposto."}
    def liberar_mensal(self, origem):
        if origem not in self.herancas: return {"erro": "Herança não configurada"}
        h = self.herancas[origem]
        if h['liberado'] >= h['total']: return {"erro": "Herança totalmente liberada"}
        h['liberado'] += h['mensal']
        self.salvar()
        return {"ok": True, "liberado": h['mensal'], "total_liberado': h['liberado'], 'restante': h['total'] - h['liberado']}
print("✅ UBC LIVING WILL pronto")
