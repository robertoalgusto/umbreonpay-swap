#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   BOLETO DESCENTRALIZADO                 ║
║   Emissão sem registro no BC             ║
╚══════════════════════════════════════════╝
"""
import json, os, secrets, hashlib
from datetime import datetime, timedelta

class BoletoDescentralizado:
    def __init__(self):
        self.boletos = {}
        self.carregar()
    
    def carregar(self):
        if os.path.exists('boletos.json'):
            with open('boletos.json') as f:
                self.boletos = json.load(f)
    
    def salvar(self):
        with open('boletos.json', 'w') as f:
            json.dump(self.boletos, f, indent=2)
    
    def gerar(self, valor, descricao, vencimento_dias=3):
        codigo = secrets.token_hex(16)
        vencimento = (datetime.now() + timedelta(days=vencimento_dias)).strftime("%d/%m/%Y")
        boleto = {
            "codigo": codigo,
            "valor": valor,
            "descricao": descricao,
            "vencimento": vencimento,
            "status": "pendente",
            "criado_em": datetime.now().isoformat(),
            "linha_digitavel": f"34191.79001 01043.510047 91020.150008 8 {codigo[:10]}"
        }
        self.boletos[codigo] = boleto
        self.salvar()
        return boleto
    
    def pagar(self, codigo, pagador):
        if codigo not in self.boletos: return {"erro": "Boleto não encontrado"}
        b = self.boletos[codigo]
        if b['status'] == 'pago': return {"erro": "Boleto já pago"}
        b['status'] = 'pago'
        b['pagador'] = pagador
        b['pago_em'] = datetime.now().isoformat()
        self.salvar()
        return {"ok": True, "valor": b['valor'], "descricao": b['descricao']}

print("✅ Boleto Descentralizado pronto")
