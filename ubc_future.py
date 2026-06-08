#!/usr/bin/env python3
"""UBC FUTURE — Mande dinheiro para seu eu do futuro"""
import json, os
from datetime import datetime, timedelta

class UBCFuture:
    def __init__(self):
        self.transacoes = {}
        self.carregar()
    def carregar(self):
        if os.path.exists('future.json'):
            with open('future.json') as f: self.transacoes = json.load(f)
    def salvar(self):
        with open('future.json', 'w') as f: json.dump(self.transacoes, f, indent=2)
    def agendar(self, origem, destino, valor, data_liberacao):
        tid = f"FUTURE-{datetime.now().timestamp()}"
        self.transacoes[tid] = {"origem": origem, "destino": destino, "valor": valor, "liberacao": data_liberacao, "status": "bloqueado"}
        self.salvar()
        return {"ok": True, "id": tid, "mensagem": f"R$ {valor:.2f} será enviado em {data_liberacao}"}
    def processar(self):
        liberados = []
        for tid, t in list(self.transacoes.items()):
            if t['status'] == 'bloqueado' and datetime.now().isoformat() >= t['liberacao']:
                t['status'] = 'liberado'
                liberados.append(t)
        self.salvar()
        return {"ok": True, "liberados": len(liberados)}
print("✅ UBC FUTURE pronto")
