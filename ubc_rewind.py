#!/usr/bin/env python3
"""UBC Rewind — Desfazer transação em 60s pagando 10%"""
import json, os
from datetime import datetime, timedelta

class UBCRewind:
    TAXA_REWIND = 0.10
    JANELA_SEGUNDOS = 60
    def __init__(self):
        self.transacoes = {}
    def enviar(self, origem, destino, valor):
        tid = secrets.token_hex(8)
        self.transacoes[tid] = {"origem": origem, "destino": destino, "valor": valor, "timestamp": datetime.now().isoformat(), "status": "enviada"}
        return {"ok": True, "id": tid, "rewind_disponivel_ate": (datetime.now() + timedelta(seconds=self.JANELA_SEGUNDOS)).isoformat()}
    def desfazer(self, tid):
        if tid not in self.transacoes: return {"erro": "Transação não encontrada"}
        tx = self.transacoes[tid]
        if (datetime.now() - datetime.fromisoformat(tx['timestamp'])).seconds > self.JANELA_SEGUNDOS: return {"erro": "Janela de 60s expirada"}
        taxa = tx['valor'] * self.TAXA_REWIND
        tx['status'] = 'desfeita'
        return {"ok": True, "recuperado": tx['valor'] - taxa, "taxa_rewind": taxa}
print("✅ UBC Rewind pronto")
