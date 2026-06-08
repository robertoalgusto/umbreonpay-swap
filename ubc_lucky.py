#!/usr/bin/env python3
"""UBC Lucky — Transação premiada aleatória"""
import secrets, random

class UBCLucky:
    PREMIO_INTERVALO = 1000000
    def __init__(self):
        self.contador = 0
        self.fundo_premio = 0
    def processar(self, valor):
        self.contador += 1
        self.fundo_premio += valor * 0.001
        if self.contador % self.PREMIO_INTERVALO == 0:
            premio = self.fundo_premio * 0.5
            self.fundo_premio -= premio
            return {"ok": True, "premiado": True, "premio": round(premio, 2), "mensagem": "🎉 Transação premiada! Você ganhou o dobro!"}
        return {"ok": True, "premiado": False}
print("✅ UBC Lucky pronto")
