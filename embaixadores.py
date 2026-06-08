#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   PROGRAMA DE EMBAIXADORES               ║
║   Agentes recrutam e ganham              ║
╚══════════════════════════════════════════╝
"""
import json, os
from datetime import datetime

class Embaixadores:
    COMISSOES = {1: 50, 2: 75, 3: 100}
    
    def __init__(self):
        self.embaixadores = {}
        self.indicacoes = {}
        self.carregar()
    
    def carregar(self):
        if os.path.exists('embaixadores.json'):
            with open('embaixadores.json') as f:
                d = json.load(f)
                self.embaixadores = d.get('embaixadores', {})
                self.indicacoes = d.get('indicacoes', {})
    
    def salvar(self):
        with open('embaixadores.json', 'w') as f:
            json.dump({'embaixadores': self.embaixadores, 'indicacoes': self.indicacoes}, f, indent=2)
    
    def cadastrar(self, carteira, nome):
        self.embaixadores[carteira] = {"nome": nome, "nivel": 1, "total_indicacoes": 0, "total_ganho": 0, "rede": []}
        self.salvar()
        return {"ok": True, "codigo": f"UB-EMB-{carteira[-8:].upper()}"}
    
    def indicar(self, embaixador_carteira, novo_usuario):
        if embaixador_carteira not in self.embaixadores: return {"erro": "Embaixador não encontrado"}
        e = self.embaixadores[embaixador_carteira]
        e['total_indicacoes'] += 1
        if e['total_indicacoes'] >= 51: e['nivel'] = 3
        elif e['total_indicacoes'] >= 11: e['nivel'] = 2
        comissao = self.COMISSOES.get(e['nivel'], 50)
        e['total_ganho'] += comissao
        e['rede'].append(novo_usuario)
        self.indicacoes[novo_usuario] = embaixador_carteira
        self.salvar()
        return {"ok": True, "comissao": comissao, "nivel": e['nivel'], "total_ganho": e['total_ganho']}

print("✅ Embaixadores pronto")
