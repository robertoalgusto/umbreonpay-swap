#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   CRÉDITO COLABORATIVO UBC               ║
║   Usuários emprestam para usuários       ║
╚══════════════════════════════════════════╝
"""
import json, os
from datetime import datetime

class CreditoColaborativo:
    JUROS = 0.03  # 3% ao mês
    
    def __init__(self):
        self.ofertas = []  # Quem quer emprestar
        self.emprestimos = []  # Empréstimos ativos
        self.carregar()
    
    def carregar(self):
        if os.path.exists('credito.json'):
            with open('credito.json') as f:
                d = json.load(f)
                self.ofertas = d.get('ofertas', [])
                self.emprestimos = d.get('emprestimos', [])
    
    def salvar(self):
        with open('credito.json', 'w') as f:
            json.dump({'ofertas': self.ofertas, 'emprestimos': self.emprestimos}, f, indent=2)
    
    def oferecer_credito(self, carteira, valor, juros=3.0):
        self.ofertas.append({"carteira": carteira, "valor": valor, "juros": juros, "status": "disponivel"})
        self.salvar()
        return {"ok": True, "mensagem": f"Oferta de {valor} UBC a {juros}% ao mês"}
    
    def pegar_emprestimo(self, carteira, valor):
        for oferta in self.ofertas:
            if oferta['valor'] >= valor and oferta['status'] == 'disponivel':
                oferta['status'] = 'emprestado'
                self.emprestimos.append({"devedor": carteira, "credor": oferta['carteira'], "valor": valor, "juros": oferta['juros'], "data": datetime.now().isoformat(), "status": "ativo"})
                self.salvar()
                return {"ok": True, "mensagem": f"Empréstimo de {valor} UBC a {oferta['juros']}%"}
        return {"erro": "Sem ofertas disponíveis"}

print("✅ Crédito Colaborativo pronto")
