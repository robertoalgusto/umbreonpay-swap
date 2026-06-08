#!/usr/bin/env python3
"""UBC WALK — Ande e ganhe dinheiro"""
class UBCWalk:
    UBC_POR_10000_PASSOS = 0.1
    def __init__(self):
        self.total_passos = 0
        self.ubc_ganho = 0
    def registrar_passos(self, passos):
        self.total_passos += passos
        ganho = (passos // 10000) * self.UBC_POR_10000_PASSOS
        self.ubc_ganho += ganho
        return {"ok": True, "passos": passos, "ganho": ganho, "total_ubc": self.ubc_ganho}
print("✅ UBC WALK pronto")
