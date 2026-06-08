#!/usr/bin/env python3
"""UBC BLINK — Piscar como confirmação"""
class UBCBlink:
    def autorizar(self, valor, piscadas):
        if valor > 1000 and piscadas != 3:
            return {"autorizado": False, "motivo": "Para transações acima de R$ 1.000, pisque 3 vezes"}
        return {"autorizado": True, "piscadas": piscadas, "seguranca": "Sob coação você não pisca naturalmente"}
print("✅ UBC BLINK pronto")
