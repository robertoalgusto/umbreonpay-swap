#!/usr/bin/env python3
"""UBC NEGOTIATOR — IA que negocia dívidas"""
class UBCNegotiator:
    def negociar(self, devedor, credor, valor_devido):
        proposta = round(valor_devido * 0.80, 2)
        return {"ok": True, "proposta": f"Pague {proposta} UBC agora e quite a dívida de {valor_devido} UBC", "desconto": f"{20}%", "valido_ate": "24 horas"}
print("✅ UBC NEGOTIATOR pronto")
