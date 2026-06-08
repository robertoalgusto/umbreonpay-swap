#!/usr/bin/env python3
"""UBC Quantum — Endereço que muda a cada transação"""
import secrets, hashlib

class UBCQuantum:
    def __init__(self):
        self.carteiras = {}
    def criar(self, titular):
        seed = secrets.token_hex(64)
        self.carteiras[titular] = {"seed": seed, "contador": 0, "enderecos": []}
        return {"ok": True, "titular": titular}
    def novo_endereco(self, titular):
        if titular not in self.carteiras: return {"erro": "Carteira não encontrada"}
        c = self.carteiras[titular]
        c['contador'] += 1
        end = "UBC-Q-" + hashlib.sha3_256(f"{c['seed']}{c['contador']}".encode()).hexdigest()[:32]
        c['enderecos'].append(end)
        return {"ok": True, "endereco": end, "contador": c['contador'], "privacidade": "Endereço nunca se repete"}
print("✅ UBC Quantum pronto")
