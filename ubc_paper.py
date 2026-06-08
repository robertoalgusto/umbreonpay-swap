#!/usr/bin/env python3
"""UBC PAPER — Carteira de papel offline"""
import secrets, hashlib
class UBCPaper:
    def gerar(self, valor):
        chave_privada = secrets.token_hex(32)
        chave_publica = hashlib.sha3_256(chave_privada.encode()).hexdigest()[:32]
        return {"ok": True, "chave_publica": chave_publica, "chave_privada": chave_privada, "instrucao": "Imprima e guarde em local seguro. Sem dispositivo eletrônico."}
print("✅ UBC PAPER pronto")
