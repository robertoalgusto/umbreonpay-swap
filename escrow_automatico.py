#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   ESCROW AUTOMÁTICO (UBC TRADE)          ║
║   Custódia entre comprador e vendedor    ║
╚══════════════════════════════════════════╝
"""
import json, os, secrets
from datetime import datetime, timedelta

class EscrowAutomatico:
    def __init__(self):
        self.negocios = {}
        self.carregar()
    
    def carregar(self):
        if os.path.exists('escrow.json'):
            with open('escrow.json') as f:
                self.negocios = json.load(f)
    
    def salvar(self):
        with open('escrow.json', 'w') as f:
            json.dump(self.negocios, f, indent=2)
    
    def criar(self, vendedor, comprador, valor, descricao, prazo_horas=72):
        codigo = secrets.token_hex(8)
        self.negocios[codigo] = {"vendedor": vendedor, "comprador": comprador, "valor": valor, "descricao": descricao, "status": "aguardando_pagamento", "prazo": (datetime.now() + timedelta(hours=prazo_horas)).isoformat(), "criado_em": datetime.now().isoformat()}
        self.salvar()
        return {"ok": True, "codigo": codigo, "mensagem": f"Escrow criado: {descricao} — {valor} UBC"}
    
    def comprador_pagou(self, codigo):
        if codigo not in self.negocios: return {"erro": "Escrow não encontrado"}
        self.negocios[codigo]['status'] = 'pago_aguardando_confirmacao'
        self.salvar()
        return {"ok": True, "status": "Dinheiro retido. Vendedor deve entregar o produto."}
    
    def comprador_confirmou(self, codigo):
        if codigo not in self.negocios: return {"erro": "Escrow não encontrado"}
        self.negocios[codigo]['status'] = 'concluido'
        self.salvar()
        return {"ok": True, "status": "UBC liberado para o vendedor. Negócio concluído!"}
    
    def abrir_disputa(self, codigo):
        if codigo not in self.negocios: return {"erro": "Escrow não encontrado"}
        self.negocios[codigo]['status'] = 'em_disputa'
        self.salvar()
        return {"ok": True, "status": "Disputa aberta. Árbitro Umbreon vai analisar."}

print("✅ Escrow Automático pronto")
