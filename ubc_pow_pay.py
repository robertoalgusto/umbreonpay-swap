#!/usr/bin/env python3
"""UBC POW-PAY — Pague com processamento, não com dinheiro"""
import secrets, hashlib, time, json, os

class UBCPowPay:
    DIFICULDADE = 4
    def __init__(self):
        self.transacoes = []
    def minerar_pagamento(self, valor_ubc, destino, tempo_max=30):
        inicio = time.time()
        nonce = 0
        while time.time() - inicio < tempo_max:
            hash_tentativa = hashlib.sha256(f"{valor_ubc}{destino}{nonce}".encode()).hexdigest()
            if hash_tentativa.startswith("0" * self.DIFICULDADE):
                self.transacoes.append({"valor": valor_ubc, "destino": destino, "nonce": nonce, "tempo": round(time.time() - inicio, 1), "hash": hash_tentativa[:16]})
                return {"ok": True, "pago_com": "processamento", "tempo_gasto": round(time.time() - inicio, 1), "valor": valor_ubc}
            nonce += 1
        return {"erro": "Tempo esgotado"}
print("✅ UBC POW-PAY pronto")
