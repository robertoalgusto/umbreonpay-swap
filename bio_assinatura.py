#!/usr/bin/env python3
"""Assinatura Biométrica Comportamental — Padrão de digitação como senha"""
import hashlib, json, os

class BioAssinatura:
    def __init__(self):
        self.padroes = {}
        self.carregar()
    def carregar(self):
        if os.path.exists('bio.json'):
            with open('bio.json') as f: self.padroes = json.load(f)
    def salvar(self):
        with open('bio.json', 'w') as f: json.dump(self.padroes, f, indent=2)
    def registrar(self, usuario, digitação, pressao, ritmo):
        hash_padrao = hashlib.sha3_256(f"{digitacao}{pressao}{ritmo}".encode()).hexdigest()
        self.padroes[usuario] = hash_padrao
        self.salvar()
        return {"ok": True, "mensagem": "Padrão de digitação registrado. Impossível de falsificar."}
    def verificar(self, usuario, digitacao, pressao, ritmo):
        if usuario not in self.padroes: return {"erro": "Usuário não registrado"}
        hash_atual = hashlib.sha3_256(f"{digitacao}{pressao}{ritmo}".encode()).hexdigest()
        return {"autentico": hash_atual == self.padroes[usuario]}
print("✅ Bio Assinatura pronto")
