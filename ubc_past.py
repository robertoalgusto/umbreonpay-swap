#!/usr/bin/env python3
"""UBC PAST — Prova retroativa de posse"""
import hashlib
from datetime import datetime

class UBCPast:
    def __init__(self):
        self.registros = {}
    def registrar_saldo(self, usuario, saldo):
        timestamp = datetime.now().isoformat()
        hash_prova = hashlib.sha3_256(f"{usuario}{saldo}{timestamp}".encode()).hexdigest()
        self.registros[usuario] = {"saldo": saldo, "timestamp": timestamp, "hash": hash_prova}
        return {"ok": True, "hash": hash_prova[:16], "mensagem": "Prova de saldo registrada. Válida para auditorias futuras."}
    def provar(self, usuario, data_consulta):
        if usuario in self.registros:
            return {"ok": True, "saldo_em": self.registros[usuario]['timestamp'], "saldo": self.registros[usuario]['saldo']}
        return {"erro": "Sem registro"}
print("✅ UBC PAST pronto")
