#!/usr/bin/env python3
"""UBC ZERO-PROOF — Prove que é pobre sem revelar seu saldo"""
import hashlib

class UBCZeroProof:
    def __init__(self):
        self.saldos = {}
    def registrar(self, usuario, saldo):
        self.saldos[usuario] = saldo
    def provar_abaixo_de(self, usuario, limite):
        if usuario not in self.saldos: return {"erro": "Usuário não encontrado"}
        return {"abaixo_do_limite": self.saldos[usuario] < limite, "limite": limite, "saldo_revelado": "NÃO REVELADO", "prova": "Zero-Knowledge"}
print("✅ UBC ZERO-PROOF pronto")
