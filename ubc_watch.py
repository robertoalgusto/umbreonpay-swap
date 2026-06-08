#!/usr/bin/env python3
"""UBC WATCH — Sua atenção vira moeda"""
import json, os
class UBCWatch:
    VALOR_POR_ANUNCIO = 0.01
    def __init__(self):
        self.assistidos = 0
        self.saldo = 0
    def assistir_anuncio(self, duracao=15):
        if duracao >= 15:
            self.assistidos += 1
            self.saldo += self.VALOR_POR_ANUNCIO
            return {"ok": True, "ganho": self.VALOR_POR_ANUNCIO, "saldo": self.saldo, "total_anuncios": self.assistidos}
        return {"erro": "Anúncio precisa ter no mínimo 15 segundos"}
print("✅ UBC WATCH pronto")
