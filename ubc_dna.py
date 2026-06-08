#!/usr/bin/env python3
"""UBC DNA — Distribuição algorítmica de herança"""
import json, os
from datetime import datetime, timedelta

class UBCDNA:
    def __init__(self):
        self.herancas = {}
        self.carregar()
    def carregar(self):
        if os.path.exists('dna.json'):
            with open('dna.json') as f: self.herancas = json.load(f)
    def salvar(self):
        with open('dna.json', 'w') as f: json.dump(self.herancas, f, indent=2)
    def configurar(self, origem, algoritmo):
        self.herancas[origem] = algoritmo
        self.salvar()
        return {"ok": True, "algoritmo": algoritmo}
    def executar(self, origem, saldo):
        if origem not in self.herancas: return {"erro": "Algoritmo não configurado"}
        dist = {}
        for herdeiro, pct in self.herancas[origem].items():
            dist[herdeiro] = round(saldo * pct / 100, 2)
        return {"ok": True, "distribuicao": dist}
print("✅ UBC DNA pronto")
