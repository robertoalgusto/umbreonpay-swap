#!/usr/bin/env python3
"""UBC MUTE — Desconecte-se e lucre"""
from datetime import datetime, timedelta
class UBCMute:
    UBC_POR_24H_SILENCIO = 0.1
    def __init__(self):
        self.sessoes = {}
    def iniciar_silencio(self, usuario):
        self.sessoes[usuario] = datetime.now().isoformat()
        return {"ok": True, "mensagem": "24h sem redes sociais. Ganhe 0.1 UBC."}
    def verificar_silencio(self, usuario):
        if usuario not in self.sessoes: return {"erro": "Silêncio não iniciado"}
        horas = (datetime.now() - datetime.fromisoformat(self.sessoes[usuario])).total_seconds() / 3600
        if horas >= 24:
            del self.sessoes[usuario]
            return {"ok": True, "ganho": self.UBC_POR_24H_SILENCIO, "mensagem": "Você ficou 24h offline. Mereceu."}
        return {"faltam": round(24 - horas, 1), "horas": round(horas, 1)}
print("✅ UBC MUTE pronto")
