#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   PAGAMENTO RECORRENTE INVISÍVEL         ║
║   Assinaturas pagas automaticamente      ║
╚══════════════════════════════════════════╝
"""
import json, os
from datetime import datetime, timedelta

class PagamentoRecorrente:
    def __init__(self):
        self.assinaturas = {}
        self.carregar()
    
    def carregar(self):
        if os.path.exists('recorrentes.json'):
            with open('recorrentes.json') as f:
                self.assinaturas = json.load(f)
    
    def salvar(self):
        with open('recorrentes.json', 'w') as f:
            json.dump(self.assinaturas, f, indent=2)
    
    def criar(self, carteira, descricao, valor, intervalo_dias=30):
        proxima = (datetime.now() + timedelta(days=intervalo_dias)).isoformat()
        self.assinaturas[descricao] = {"carteira": carteira, "valor": valor, "intervalo": intervalo_dias, "proximo": proxima, "ativo": True}
        self.salvar()
        return {"ok": True, "mensagem": f"Pagamento recorrente: {descricao} — {valor} UBC a cada {intervalo_dias} dias"}
    
    def processar(self):
        agora = datetime.now().isoformat()
        pagos = []
        for desc, a in self.assinaturas.items():
            if a['ativo'] and agora >= a['proximo']:
                a['proximo'] = (datetime.now() + timedelta(days=a['intervalo'])).isoformat()
                pagos.append({"descricao": desc, "valor": a['valor']})
        self.salvar()
        return {"ok": True, "pagos": pagos}

print("✅ Pagamento Recorrente pronto")
