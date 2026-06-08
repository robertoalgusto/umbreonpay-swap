#!/usr/bin/env python3
"""CRÉDITO POR REPUTAÇÃO — Score baseado em histórico"""
class CreditoReputacao:
    def calcular_limite(self, usuario, transacoes, dias_uso, indicacoes):
        score = (transacoes * 2) + (dias_uso * 1) + (indicacoes * 10)
        limite = min(score * 100, 50000)
        return {"ok": True, "usuario": usuario, "score": score, "limite_credito": limite, "juros": "3% ao mês", "aprovado": "Instantâneo"}
print("✅ Crédito por Reputação pronto")
