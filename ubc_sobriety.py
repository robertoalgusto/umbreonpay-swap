#!/usr/bin/env python3
"""UBC SOBRIETY — Modo de economia forçada"""
class UBCSobriety:
    def ativar(self, categorias=["bebida","jogos","apostas"], dias=30):
        return {"ok": True, "categorias_bloqueadas": categorias, "dias": dias, "multa_quebra": "10 UBC", "objetivo": "Economia forçada para sair do vício"}
print("✅ Sobriety pronto")
