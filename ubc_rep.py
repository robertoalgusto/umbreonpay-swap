#!/usr/bin/env python3
"""UBC REP — Sua confiança vale dinheiro"""
import json, os

class UBCRep:
    def __init__(self):
        self.scores = {}
        self.carregar()
    def carregar(self):
        if os.path.exists('rep.json'):
            with open('rep.json') as f: self.scores = json.load(f)
    def salvar(self):
        with open('rep.json', 'w') as f: json.dump(self.scores, f, indent=2)
    def calcular_score(self, usuario, transacoes, dias_uso, indicacoes):
        score = (transacoes * 2) + (dias_uso * 1) + (indicacoes * 10)
        self.scores[usuario] = score
        beneficios = {"score": score}
        if score >= 500: beneficios['credito_instantaneo'] = True
        if score >= 100: beneficios['parcelamento'] = "10x"
        elif score >= 50: beneficios['parcelamento'] = "5x"
        else: beneficios['parcelamento'] = "3x"
        self.salvar()
        return {"ok": True, "score": score, "beneficios": beneficios}
print("✅ UBC REP pronto")
