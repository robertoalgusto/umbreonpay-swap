#!/usr/bin/env python3
"""QUEBRA DE SENHAS — Análise de Entropia"""
class QuebraEntropia:
    def medir(self, senha):
        entropia = len(senha) * 4.7
        return {"ok": True, "senha": "***", "entropia_bits": round(entropia,1), "quebra_em": "minutos" if entropia < 40 else "horas" if entropia < 60 else "dias" if entropia < 80 else "séculos"}
print("✅ Entropia pronto")
