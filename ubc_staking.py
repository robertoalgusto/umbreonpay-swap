#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   UBC STAKING — RENDA PASSIVA            ║
║   Bloqueie UBC e receba juros            ║
╚══════════════════════════════════════════╝
"""
import json, os
from datetime import datetime, timedelta

class UBCStaking:
    TAXAS = {30: 0.03, 90: 0.05, 180: 0.08, 365: 0.15}
    
    def __init__(self):
        self.stakes = {}
        self.carregar()
    
    def carregar(self):
        if os.path.exists('staking.json'):
            with open('staking.json') as f:
                self.stakes = json.load(f)
    
    def salvar(self):
        with open('staking.json', 'w') as f:
            json.dump(self.stakes, f, indent=2)
    
    def bloquear(self, carteira, valor, dias):
        if dias not in self.TAXAS: return {"erro": "Prazo inválido"}
        taxa = self.TAXAS[dias]
        liberacao = (datetime.now() + timedelta(days=dias)).isoformat()
        stake = {"carteira": carteira, "valor": valor, "taxa": taxa, "dias": dias, "liberacao": liberacao, "status": "ativo"}
        self.stakes[liberacao] = stake
        self.salvar()
        return {"ok": True, "valor_bloqueado": valor, "rendimento": f"{taxa*100}%", "liberacao": liberacao}
    
    def resgatar(self, carteira):
        for key, s in list(self.stakes.items()):
            if s['carteira'] == carteira and s['status'] == 'ativo':
                if datetime.now().isoformat() >= s['liberacao']:
                    valor_final = s['valor'] * (1 + s['taxa'])
                    s['status'] = 'resgatado'
                    self.salvar()
                    return {"ok": True, "valor_original": s['valor'], "rendimento": valor_final - s['valor'], "valor_final": valor_final}
        return {"erro": "Nenhum stake disponível para resgate"}

print("✅ UBC Staking pronto")
