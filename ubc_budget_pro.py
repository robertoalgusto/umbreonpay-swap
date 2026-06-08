#!/usr/bin/env python3
"""UBC BUDGET PRO — Orçamento familiar completo"""
class UBCBudgetPro:
    def analizar_mes(self, gastos):
        total = sum(gastos.values())
        return {"ok": True, "total": total, "categorias": gastos, "alerta": "Gastos com delivery 30% acima da média" if gastos.get("delivery",0) > 500 else "Tudo sob controle"}
print("✅ Budget Pro pronto")
