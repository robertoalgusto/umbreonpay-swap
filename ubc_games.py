#!/usr/bin/env python3
"""UBC GAMES — Torneios de jogos com premiação em UBC"""
class UBCGames:
    def criar_torneio(self, jogo="Free Fire", premio=50):
        return {"ok": True, "jogo": jogo, "premio": f"{premio} UBC", "inscricao": "Grátis", "vencedor": "Verificado automaticamente por API"}
print("✅ Games pronto")
