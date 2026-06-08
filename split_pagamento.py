#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   SPLIT DE PAGAMENTO UBC                 ║
║   Dividir conta entre várias pessoas     ║
║   Cada um paga sua parte                 ║
╚══════════════════════════════════════════╝
"""
import secrets, json, os
from datetime import datetime

class SplitPagamento:
    def __init__(self):
        self.splits = {}
        self.carregar()
    
    def carregar(self):
        if os.path.exists('splits.json'):
            with open('splits.json') as f:
                self.splits = json.load(f)
    
    def salvar(self):
        with open('splits.json', 'w') as f:
            json.dump(self.splits, f, indent=2)
    
    def criar(self, descricao, valor_total, participantes):
        """Cria um split de pagamento entre N pessoas"""
        codigo = secrets.token_hex(6)
        valor_por_pessoa = round(valor_total / len(participantes), 2)
        
        split = {
            "id": codigo,
            "descricao": descricao,
            "valor_total": valor_total,
            "valor_por_pessoa": valor_por_pessoa,
            "participantes": {p: {"pago": False} for p in participantes},
            "criado_em": datetime.now().isoformat(),
            "status": "ativo"
        }
        self.splits[codigo] = split
        self.salvar()
        return split
    
    def pagar(self, codigo, participante):
        """Um participante paga sua parte"""
        if codigo not in self.splits: return {"erro": "Split não encontrado"}
        split = self.splits[codigo]
        if participante not in split['participantes']: return {"erro": "Participante não encontrado"}
        split['participantes'][participante]['pago'] = True
        split['participantes'][participante]['pago_em'] = datetime.now().isoformat()
        self.salvar()
        return {"ok": True, "participante": participante, "valor": split['valor_por_pessoa']}
    
    def status(self, codigo):
        """Verifica status do split"""
        if codigo not in self.splits: return {"erro": "Split não encontrado"}
        s = self.splits[codigo]
        total_pago = sum(1 for p in s['participantes'].values() if p['pago'])
        return {"total": len(s['participantes']), "pagos": total_pago, "faltam": len(s['participantes']) - total_pago}

print("✅ Split de Pagamento pronto")
