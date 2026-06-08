#!/usr/bin/env python3
"""CNG PIX INTERNACIONAL — Spread entre Brasil e exterior"""
import random
class CNGPixInternacional:
    def __init__(self):
        self.transacoes = 0
        self.lucro = 0
    def intermediar(self):
        valor_brl = random.randint(500, 3000)
        spread = random.uniform(0.03, 0.06)
        lucro = round(valor_brl * spread, 2)
        self.transacoes += 1
        self.lucro += lucro
        return {"ok": True, "valor_brl": valor_brl, "spread": f"{spread*100:.1f}%", "lucro": lucro, "total": self.lucro}
print("✅ CNG Pix Internacional pronto")
