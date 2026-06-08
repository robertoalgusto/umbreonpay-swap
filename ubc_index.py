#!/usr/bin/env python3
"""UBC INDEX FUND — Investimento automático diversificado"""
class UBCIndex:
    def investir(self, valor, perfil="moderado"):
        distribuicao = {"XMR":"40%","BTC":"25%","ETH":"15%","USDT":"10%","SOL":"10%"} if perfil=="moderado" else {"XMR":"70%","BTC":"20%","USDT":"10%"}
        return {"ok": True, "valor": valor, "perfil": perfil, "distribuicao": distribuicao, "gestao": "Automática — rebalanceamento mensal"}
print("✅ UBC Index Fund pronto")
