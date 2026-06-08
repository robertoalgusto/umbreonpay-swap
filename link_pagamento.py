#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   LINK DE PAGAMENTO UBC                  ║
║   URL compartilhável para receber        ║
╚══════════════════════════════════════════╝
"""

import secrets, json, os, hashlib
from datetime import datetime, timedelta

class LinkPagamento:
    def __init__(self):
        self.links = {}
        self.carregar()
    
    def carregar(self):
        if os.path.exists('links_pagamento.json'):
            with open('links_pagamento.json') as f:
                self.links = json.load(f)
    
    def salvar(self):
        with open('links_pagamento.json', 'w') as f:
            json.dump(self.links, f, indent=2)
    
    def criar(self, carteira_destino, valor_ubc, descricao="", valido_horas=24):
        """Cria um link de pagamento"""
        codigo = secrets.token_hex(8)
        
        link = {
            "id": codigo,
            "url": f"https://umbreonpay-swap.onrender.com/pagar/{codigo}",
            "carteira_destino": carteira_destino,
            "valor_ubc": valor_ubc,
            "descricao": descricao,
            "criado_em": datetime.now().isoformat(),
            "valido_ate": (datetime.now() + timedelta(hours=valido_horas)).isoformat(),
            "status": "ativo",
            "pago": False,
            "pagador": None
        }
        
        self.links[codigo] = link
        self.salvar()
        return link
    
    def pagar(self, codigo, carteira_pagador):
        """Processa o pagamento de um link"""
        if codigo not in self.links:
            return {"erro": "Link não encontrado"}
        
        link = self.links[codigo]
        
        if link['status'] != 'ativo':
            return {"erro": "Link expirado ou já pago"}
        
        if datetime.now().isoformat() > link['valido_ate']:
            link['status'] = 'expirado'
            self.salvar()
            return {"erro": "Link expirado"}
        
        link['pago'] = True
        link['pagador'] = carteira_pagador
        link['pago_em'] = datetime.now().isoformat()
        link['status'] = 'pago'
        self.salvar()
        
        return {
            "ok": True,
            "valor": link['valor_ubc'],
            "destino": link['carteira_destino'][:20] + "...",
            "descricao": link['descricao']
        }
    
    def listar_ativos(self, carteira):
        """Lista links ativos de uma carteira"""
        ativos = []
        for codigo, link in self.links.items():
            if link['carteira_destino'] == carteira and link['status'] == 'ativo':
                ativos.append({
                    "codigo": codigo,
                    "url": link['url'],
                    "valor": link['valor_ubc'],
                    "descricao": link['descricao'],
                    "valido_ate": link['valido_ate']
                })
        return ativos

# Teste
if __name__ == "__main__":
    lp = LinkPagamento()
    link = lp.criar("UBC-CARTEIRA-TESTE", 50, "Pagamento do freelance")
    print(f"✅ Link criado: {link['url']}")
    print(f"   Valor: {link['valor_ubc']} UBC")
    print(f"   Válido até: {link['valido_ate']}")
    
    resultado = lp.pagar(link['id'], "UBC-PAGADOR-TESTE")
    print(f"✅ Pagamento: {resultado}")
