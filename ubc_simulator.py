#!/usr/bin/env python3
"""UBC SIMULATOR — Treine investimentos sem arriscar dinheiro real"""
class UBCSimulator:
    def iniciar_simulacao(self, capital_virtual=1000):
        return {"ok": True, "capital_virtual": capital_virtual, "dinheiro_real_em_risco": "ZERO", "objetivo": "Aprender a investir antes de usar dinheiro real"}
print("✅ Simulator pronto")
