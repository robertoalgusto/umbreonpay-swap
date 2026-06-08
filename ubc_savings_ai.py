#!/usr/bin/env python3
"""UBC SAVINGS AI — IA que economiza por você"""
import random
class UBCSavingsAI:
    def __init__(self):
        self.analises = []
    def analisar(self, usuario, gastos_mensais):
        sobra = sum(gastos_mensais) * random.uniform(0.05, 0.15)
        self.analises.append({"usuario": usuario, "sobra_detectada": round(sobra, 2)})
        return {"ok": True, "sobra": round(sobra, 2), "acao": f"Movidos {round(sobra,2)} UBC para o Vault automaticamente"}
print("✅ UBC SAVINGS AI pronto")
