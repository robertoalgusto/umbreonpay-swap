#!/usr/bin/env python3
import random, json, os
from datetime import datetime

class MatchingEngine:
    def __init__(self):
        self.fornecedores = []
        if os.path.exists("fornecedores.json"):
            with open("fornecedores.json") as f:
                self.fornecedores = json.load(f)
    def salvar(self):
        with open("fornecedores.json","w") as f:
            json.dump(self.fornecedores, f, indent=2)
    def buscar_melhor(self, valor):
        d = [f for f in self.fornecedores if f.get("status")=="ativo" and f.get("limite",0)>=valor]
        if not d: return None
        d.sort(key=lambda x: x.get("taxa",99))
        return d[0]

engine = MatchingEngine()
if not engine.fornecedores:
    engine.fornecedores = [
        {"id":"F001","nome":"Maria","pix":"maria@email.com","taxa":2.0,"limite":5000,"score":98,"status":"ativo"},
        {"id":"F002","nome":"João","pix":"joao@email.com","taxa":3.0,"limite":500,"score":85,"status":"ativo"}
    ]
    engine.salvar()
print("✅ Matching Engine pronto")
