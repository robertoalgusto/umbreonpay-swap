#!/usr/bin/env python3
"""UBC DAILY TIP — Dica financeira todo dia"""
import random
class UBCDailyTip:
    def dica_do_dia(self):
        dicas = ["Hoje é um bom dia para comprar XMR","Evite sacar nas segundas — taxas maiores","Configure o Vault para economizar sem pensar","Use o Modo Fantasma quando estiver em público"]
        return {"ok": True, "dica": random.choice(dicas), "frequencia": "Todo dia às 08:00"}
print("✅ Daily Tip pronto")
