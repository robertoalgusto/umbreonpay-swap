#!/usr/bin/env python3
"""UBC GLOSSARY — Dicionário de termos cripto"""
class UBCGlossary:
    def buscar(self, termo):
        termos = {"DeFi":"Finanças Descentralizadas","staking":"Render juros bloqueando cripto","XMR":"Monero — criptomoeda anônima","UBC":"Umbreon Coin — lastreada em XMR"}
        return {"ok": True, "termo": termo, "definicao": termos.get(termo, "Termo não encontrado — sugira ao suporte")}
print("✅ Glossary pronto")
