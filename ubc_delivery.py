#!/usr/bin/env python3
"""UBC DELIVERY — Parceria com iFood, Uber Eats, Rappi"""
class UBCDelivery:
    def pagar_pedido(self, valor, app="iFood"):
        cashback = round(valor * 0.05, 2)
        return {"ok": True, "app": app, "valor": valor, "cashback": cashback, "pagamento": "UBC convertido automaticamente"}
print("✅ Delivery pronto")
