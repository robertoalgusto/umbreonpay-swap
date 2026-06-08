#!/usr/bin/env python3
"""UBC VOTE — Democracia líquida e privada"""
import secrets

class UBCVote:
    def __init__(self):
        self.votacoes = {}
    def criar_votacao(self, titulo, opcoes):
        votacao_id = secrets.token_hex(8)
        self.votacoes[votacao_id] = {"titulo": titulo, "opcoes": {o: 0 for o in opcoes}, "votantes": []}
        return {"ok": True, "id": votacao_id}
    def votar(self, votacao_id, usuario, opcao):
        if votacao_id not in self.votacoes: return {"erro": "Votação não encontrada"}
        if usuario in self.votacoes[votacao_id]['votantes']: return {"erro": "Você já votou"}
        self.votacoes[votacao_id]['opcoes'][opcao] += 1
        self.votacoes[votacao_id]['votantes'].append(usuario)
        return {"ok": True, "anonimo": True}
    def resultado(self, votacao_id):
        if votacao_id not in self.votacoes: return {"erro": "Votação não encontrada"}
        return {"ok": True, "resultado": self.votacoes[votacao_id]['opcoes'], "total_votos": len(self.votacoes[votacao_id]['votantes'])}
print("✅ UBC VOTE pronto")
