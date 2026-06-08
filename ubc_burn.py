#!/usr/bin/env python3
"""UBC BURN — Suor vira capital"""
class UBCBurn:
    UBC_POR_500_CALORIAS = 0.5
    def __init__(self):
        self.total_calorias = 0
        self.ubc_ganho = 0
    def registrar_calorias(self, calorias):
        self.total_calorias += calorias
        ganho = (calorias // 500) * self.UBC_POR_500_CALORIAS
        self.ubc_ganho += ganho
        return {"ok": True, "calorias": calorias, "ganho": ganho, "total_ubc": self.ubc_ganho}
print("✅ UBC BURN pronto")
