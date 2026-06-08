#!/usr/bin/env python3
"""UBC PULSE — Batimento cardíaco como senha"""
import hashlib
class UBCPulse:
    def __init__(self):
        self.padroes = {}
    def registrar(self, usuario, batimento_bpm):
        self.padroes[usuario] = hashlib.sha256(str(batimento_bpm).encode()).hexdigest()
        return {"ok": True, "mensagem": "Seu coração é a senha. Se você morrer, o dinheiro vai para o herdeiro."}
    def verificar(self, usuario, batimento_atual):
        return {"autentico": hashlib.sha256(str(batimento_atual).encode()).hexdigest() == self.padroes.get(usuario, "")}
print("✅ UBC PULSE pronto")
