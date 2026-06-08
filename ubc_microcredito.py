#!/usr/bin/env python3
"""MICROCRÉDITO — Para ambulantes, feirantes, prestadores de serviço"""
class Microcredito:
    def conceder(self, valor, atividade):
        return {"ok": True, "valor": valor, "atividade": atividade, "juros": "1.5% ao mês", "burocracia": "ZERO", "requisito": "Apenas histórico de transações no UmbreonPay", "aprovacao": "Instantânea"}
print("✅ Microcrédito pronto")
