#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   DÉBITO AUTOMÁTICO UBC                  ║
║   Contas pagas sozinhas                  ║
╚══════════════════════════════════════════╝
"""
import json, os
from datetime import datetime

class DebitoAutomatico:
    def __init__(self):
        self.debitos = {}
        self.carregar()
    
    def carregar(self):
        if os.path.exists('debitos.json'):
            with open('debitos.json') as f:
                self.debitos = json.load(f)
    
    def salvar(self):
        with open('debitos.json', 'w') as f:
            json.dump(self.debitos, f, indent=2)
    
    def cadastrar(self, carteira, descricao, valor, dia_vencimento):
        self.debitos[descricao] = {"carteira": carteira, "valor": valor, "dia": dia_vencimento, "ativo": True, "ultimo_pagamento": None}
        self.salvar()
        return {"ok": True, "mensagem": f"Débito automático cadastrado: {descricao} — R$ {valor:.2f} todo dia {dia_vencimento}"}
    
    def processar(self):
        hoje = datetime.now().day
        pagos = []
        for desc, d in self.debitos.items():
            if d['ativo'] and d['dia'] == hoje:
                d['ultimo_pagamento'] = datetime.now().isoformat()
                pagos.append({"descricao": desc, "valor": d['valor']})
        self.salvar()
        return {"ok": True, "processados": len(pagos), "pagos": pagos}

print("✅ Débito Automático pronto")
