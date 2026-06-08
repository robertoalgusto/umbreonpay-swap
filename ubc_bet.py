#!/usr/bin/env python3
"""UBC BET — Desafios físicos monetizados"""
import json, os
from datetime import datetime

class UBCBet:
    def __init__(self):
        self.desafios = {}
        self.carregar()
    def carregar(self):
        if os.path.exists('bet.json'):
            with open('bet.json') as f: self.desafios = json.load(f)
    def salvar(self):
        with open('bet.json', 'w') as f: json.dump(self.desafios, f, indent=2)
    def criar_desafio(self, usuario, descricao, aposta, prazo_horas=24):
        self.desafios[usuario] = {"descricao": descricao, "aposta": aposta, "prazo": prazo_horas, "status": "pendente", "criado_em": datetime.now().isoformat()}
        self.salvar()
        return {"ok": True, "mensagem": f"Desafio: {descricao}. Aposta: {aposta} UBC"}
    def concluir(self, usuario, sucesso):
        if usuario not in self.desafios: return {"erro": "Desafio não encontrado"}
        d = self.desafios[usuario]
        d['status'] = 'concluido'
        d['resultado'] = 'sucesso' if sucesso else 'falha'
        ganho = d['aposta'] * 2 if sucesso else -d['aposta']
        self.salvar()
        return {"ok": True, "resultado": d['resultado'], "ganho": ganho}
print("✅ UBC BET pronto")
