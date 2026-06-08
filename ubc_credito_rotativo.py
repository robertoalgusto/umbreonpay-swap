#!/usr/bin/env python3
"""CRÉDITO ROTATIVO UBC — Como cartão de crédito, mas em UBC"""
from datetime import datetime, timedelta
class CreditoRotativo:
    def __init__(self):
        self.fatura = 0
    def comprar(self, valor):
        self.fatura += valor
        return {"ok": True, "valor": valor, "fatura_atual": self.fatura, "vencimento": (datetime.now() + timedelta(days=30)).strftime("%d/%m/%Y"), "juros_atraso": "3% ao mês"}
print("✅ Crédito Rotativo pronto")
