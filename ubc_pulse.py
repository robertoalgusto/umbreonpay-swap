#!/usr/bin/env python3
"""UBC PULSE — Monitor de saúde financeira"""
class UBCPulse:
    def diagnosticar(self, usuario):
        return {"ok": True, "usuario": usuario, "score_financeiro": 78, "alerta": "Gastos com delivery 30% acima", "recomendacao": "Configure limite automático para delivery"}
print("✅ Pulse pronto")
