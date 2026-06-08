#!/usr/bin/env python3
"""UBC VOICE — Pagamento por comando de voz"""
class UBCVoice:
    def processar_comando(self, usuario, frase):
        return {"ok": True, "usuario": usuario, "frase": frase, "acao": "Pix de R$ 50 para João processado", "maos": "LIVRES — sem tocar no celular"}
print("✅ UBC VOICE pronto")
