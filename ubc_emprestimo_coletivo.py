#!/usr/bin/env python3
"""EMPRÉSTIMO COLETIVO INSTANTÂNEO — 200 pessoas emprestam R$ 5 cada"""
import random
class EmprestimoColetivo:
    def solicitar(self, valor, tomador):
        credores = random.randint(50, 200)
        valor_por_credor = round(valor / credores, 2)
        return {"ok": True, "valor": valor, "credores": credores, "valor_por_credor": valor_por_credor, "tempo": "5 segundos", "anonimato": "Ninguém sabe para quem emprestou"}
print("✅ Empréstimo Coletivo pronto")
