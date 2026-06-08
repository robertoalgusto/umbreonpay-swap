#!/usr/bin/env python3
"""UBC BUDGET — Orçamento automático"""
class UBCBudget:
    def __init__(self):
        self.orcamentos = {}
    def definir_limite(self, usuario, categoria, limite_mensal):
        self.orcamentos[usuario] = self.orcamentos.get(usuario, {})
        self.orcamentos[usuario][categoria] = {"limite": limite_mensal, "gasto": 0}
        return {"ok": True, "categoria": categoria, "limite": limite_mensal}
    def verificar_gasto(self, usuario, categoria, valor):
        if usuario in self.orcamentos and categoria in self.orcamentos[usuario]:
            o = self.orcamentos[usuario][categoria]
            if o['gasto'] + valor > o['limite']:
                return {"autorizado": False, "motivo": f"Limite de {categoria} atingido"}
            o['gasto'] += valor
        return {"autorizado": True}
print("✅ UBC BUDGET pronto")
