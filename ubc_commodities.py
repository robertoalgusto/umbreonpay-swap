#!/usr/bin/env python3
"""UBC COMMODITIES — Lastro em ouro, prata, petróleo"""
class UBCCommodities:
    def lastrear(self, ativo="ouro", porcentagem=20):
        return {"ok": True, "ativo": ativo, "lastro": f"{porcentagem}% do portfólio", "protecao": "Contra volatilidade cripto", "ativos_disponiveis": ["Ouro","Prata","Petróleo","Cobre","Lítio"]}
print("✅ UBC Commodities pronto")
