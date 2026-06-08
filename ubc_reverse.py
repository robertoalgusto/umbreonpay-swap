#!/usr/bin/env python3
"""UBC REVERSE — Vendedores competem pelo comprador"""
import secrets

class UBCReverse:
    def __init__(self):
        self.leiloes = {}
    def criar_pedido(self, comprador, item, preco_maximo, prazo_horas=24):
        leilao_id = secrets.token_hex(8)
        self.leiloes[leilao_id] = {"comprador": comprador, "item": item, "maximo": preco_maximo, "ofertas": {}, "status": "aberto"}
        return {"ok": True, "id": leilao_id, "mensagem": f"Vendedores, ofereçam abaixo de R$ {preco_maximo:.2f}"}
    def ofertar(self, leilao_id, vendedor, preco):
        if leilao_id not in self.leiloes: return {"erro": "Leilão não encontrado"}
        if preco > self.leiloes[leilao_id]['maximo']: return {"erro": "Preço acima do máximo"}
        self.leiloes[leilao_id]['ofertas'][vendedor] = preco
        return {"ok": True, "mensagem": "Oferta registrada"}
    def encerrar(self, leilao_id):
        if leilao_id not in self.leiloes: return {"erro": "Leilão não encontrado"}
        l = self.leiloes[leilao_id]
        if not l['ofertas']: return {"erro": "Sem ofertas"}
        vencedor = min(l['ofertas'], key=l['ofertas'].get)
        return {"ok": True, "vencedor": vencedor, "preco": l['ofertas'][vencedor], "comprador": l['comprador']}
print("✅ UBC REVERSE pronto")
