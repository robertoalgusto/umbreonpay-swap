#!/usr/bin/env python3
"""UBC Think — Autorização por padrão cerebral (EEG)"""
import secrets, hashlib, json, os

class UBCThink:
    def __init__(self):
        self.padroes = {}
        self.carregar()
    def carregar(self):
        if os.path.exists('think.json'):
            with open('think.json') as f: self.padroes = json.load(f)
    def salvar(self):
        with open('think.json', 'w') as f: json.dump(self.padroes, f, indent=2)
    def treinar(self, usuario, leituras_eeg):
        hash_padrao = hashlib.sha3_256(str(leituras_eeg).encode()).hexdigest()
        self.padroes[usuario] = hash_padrao
        self.salvar()
        return {"ok": True, "mensagem": "Padrão cerebral registrado. Pense 'autorizar' para pagar."}
    def autorizar(self, usuario, leitura_atual):
        if usuario not in self.padroes: return {"erro": "Usuário não treinado"}
        hash_atual = hashlib.sha3_256(str(leitura_atual).encode()).hexdigest()
        return {"autorizado": hash_atual == self.padroes[usuario], "seguranca": "Impossível forçar — o cérebro não obedece sob coação"}
print("✅ UBC Think pronto")
