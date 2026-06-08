#!/usr/bin/env python3
"""UBC DREAM — Ganhe dinheiro dormindo"""
import time, random
class UBCDream:
    UBC_POR_HORA_SONO = 0.05
    def __init__(self):
        self.sessoes = []
    def iniciar_sono(self):
        inicio = time.time()
        return {"ok": True, "inicio": inicio, "mensagem": "Durma. A SHIRA trabalha por você."}
    def finalizar_sono(self, inicio):
        horas = (time.time() - inicio) / 3600
        ganho = round(horas * self.UBC_POR_HORA_SONO, 4)
        self.sessoes.append({"horas": round(horas, 1), "ganho": ganho})
        return {"ok": True, "horas_dormidas": round(horas, 1), "ubc_ganho": ganho}
print("✅ UBC DREAM pronto")
