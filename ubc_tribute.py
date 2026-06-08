#!/usr/bin/env python3
"""UBC TRIBUTE — Homenagem póstuma com doação"""
class UBCTribute:
    def criar_memorial(self, nome_falecido, causa):
        return {"ok": True, "nome": nome_falecido, "causa": causa, "saldo_doado": "Ao atingir R$ 1.000, doação automática", "taxa": "0%"}
print("✅ Tribute pronto")
