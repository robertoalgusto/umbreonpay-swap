#!/usr/bin/env python3
"""UBC REWIND 2.0 — Janela de arrependimento de 60 segundos"""
import json, os
from datetime import datetime, timedelta

class UBCRewind2:
    TAXA = 0.10
    JANELA = 60
    def __init__(self):
        self.transacoes = {}
    def enviar(self, origem, destino, valor):
        tid = f"RW-{datetime.now().timestamp()}"
        self.transacoes[tid] = {"origem": origem, "destino": destino, "valor": valor, "timestamp": datetime.now().isoformat(), "status": "enviada"}
        return {"ok": True, "id": tid, "desfazer_ate": (datetime.now() + timedelta(seconds=self.JANELA)).strftime("%H:%M:%S")}
    def desfazer(self, tid):
        if tid not in self.transacoes: return {"erro": "Transação não encontrada"}
        t = self.transacoes[tid]
        if (datetime.now() - datetime.fromisoformat(t['timestamp'])).seconds > self.JANELA: return {"erro": "Janela de 60s expirada"}
        t['status'] = 'desfeita'
        return {"ok": True, "recuperado": round(t['valor'] * (1 - self.TAXA), 2), "taxa": round(t['valor'] * self.TAXA, 2)}
print("✅ UBC REWIND 2.0 pronto")
