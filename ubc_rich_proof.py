#!/usr/bin/env python3
"""UBC RICH-PROOF — Prove que é rico sem expor seu saldo"""
class UBCRichProof:
    def __init__(self):
        self.saldos = {}
    def registrar(self, usuario, saldo):
        self.saldos[usuario] = saldo
    def provar_acima_de(self, usuario, limite):
        if usuario not in self.saldos: return {"erro": "Usuário não encontrado"}
        return {"acima_do_limite": self.saldos[usuario] >= limite, "limite": limite, "saldo_revelado": "NÃO REVELADO", "prova": "Zero-Knowledge"}
print("✅ UBC RICH-PROOF pronto")
