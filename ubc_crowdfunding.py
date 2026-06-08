#!/usr/bin/env python3
"""UBC CROWDFUNDING — Vaquinha descentralizada"""
class UBCCrowdfunding:
    def criar_campanha(self, titulo, meta, criador):
        return {"ok": True, "titulo": titulo, "meta": meta, "criador": criador, "regra": "Se não atingir meta em 30 dias, dinheiro volta aos doadores", "taxa": "0%"}
print("✅ Crowdfunding pronto")
