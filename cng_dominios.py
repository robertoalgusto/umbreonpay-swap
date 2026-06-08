#!/usr/bin/env python3
"""CNG DOMÍNIOS — Compra e revenda de domínios"""
import random
class CNGDominios:
    def __init__(self):
        self.portfolio = []
        self.lucro = 0
    def garimpar(self):
        dominio = f"exemplo{random.randint(100,999)}.com"
        preco_compra = random.randint(10, 40)
        preco_venda = random.randint(100, 500)
        self.portfolio.append({"dominio": dominio, "compra": preco_compra, "venda": preco_venda})
        self.lucro += preco_venda - preco_compra
        return {"ok": True, "dominio": dominio, "compra": preco_compra, "venda": preco_venda, "lucro": preco_venda - preco_compra}
print("✅ CNG Domínios pronto")
