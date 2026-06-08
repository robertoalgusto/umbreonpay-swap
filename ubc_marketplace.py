#!/usr/bin/env python3
"""UBC MARKETPLACE — Marketplace anônimo peer-to-peer"""
class UBCMarketplace:
    def anunciar(self, produto, preco, vendedor):
        return {"ok": True, "produto": produto, "preco": preco, "vendedor": vendedor, "taxa": "0%", "anonimato": "Comprador e vendedor anônimos"}
print("✅ Marketplace pronto")
