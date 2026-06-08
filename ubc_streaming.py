#!/usr/bin/env python3
"""UBC STREAMING — Parceria com Netflix, Spotify, Prime Video"""
class UBCStreaming:
    def pagar_assinatura(self, servico="Netflix", meses=12):
        bonus = "1 mês grátis" if meses >= 12 else "5% de desconto"
        return {"ok": True, "servico": servico, "meses": meses, "bonus": bonus, "pagamento": "UBC convertido automaticamente"}
print("✅ Streaming pronto")
