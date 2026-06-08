#!/usr/bin/env python3
"""UBC RETIREMENT — Simulador de aposentadoria"""
class UBCRetirement:
    def simular(self, idade_atual, aporte_mensal, idade_aposentadoria=60):
        anos = idade_aposentadoria - idade_atual
        montante = aporte_mensal * 12 * anos * 1.05
        return {"ok": True, "anos_contribuindo": anos, "total_acumulado": round(montante, 2), "renda_mensal_estimada": round(montante * 0.005, 2)}
print("✅ Retirement pronto")
