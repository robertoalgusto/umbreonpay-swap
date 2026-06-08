#!/usr/bin/env python3
"""UBC FLORA — Microbioma como 2FA"""
import hashlib
class UBCFlora:
    def __init__(self):
        self.microbiomas = {}
    def registrar(self, usuario, amostra_bacterias):
        self.microbiomas[usuario] = hashlib.sha3_256(amostra_bacterias.encode()).hexdigest()
        return {"ok": True, "mensagem": "Suas bactérias são seu segundo fator de autenticação"}
print("✅ UBC FLORA pronto")
