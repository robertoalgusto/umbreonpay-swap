#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   CONVERSÃO INVISÍVEL                    ║
║   Middleware monetário automático        ║
╚══════════════════════════════════════════╝
"""
import json, os

class ConversaoInvisivel:
    REGRAS = {}
    
    @classmethod
    def configurar(cls, carteira, regra):
        cls.REGRAS[carteira] = regra
        return {"ok": True, "regra": regra}
    
    @classmethod
    def processar(cls, carteira, valor_recebido):
        if carteira not in cls.REGRAS: return {"acao": "manter_ubc", "valor": valor_recebido}
        regra = cls.REGRAS[carteira]
        resultado = {}
        for moeda, percentual in regra.items():
            resultado[moeda] = round(valor_recebido * percentual / 100, 2)
        return {"acao": "converter", "distribuicao": resultado}

print("✅ Conversão Invisível pronta")
