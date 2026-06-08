#!/usr/bin/env python3
"""CNG AFILIADO — Comissões automáticas"""
import random
class CNGAfiliado:
    PLATAFORMAS = ["Amazon", "Mercado Livre", "Shopee", "Magazine Luiza", "Aliexpress"]
    def __init__(self):
        self.vendas = 0
        self.comissao = 0
    def gerar_venda(self):
        plataforma = random.choice(self.PLATAFORMAS)
        valor = random.randint(50, 500)
        comissao = round(valor * random.uniform(0.03, 0.10), 2)
        self.vendas += 1
        self.comissao += comissao
        return {"ok": True, "plataforma": plataforma, "valor": valor, "comissao": comissao, "total": self.comissao}
print("✅ CNG Afiliado pronto")
