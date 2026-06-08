#!/usr/bin/env python3
"""UBC MULTIVERSE — E se você tivesse tomado outra decisão?"""
import random

class UBCMultiverse:
    def __init__(self):
        self.cenarios = []
    def simular(self, saldo_atual, decisao_alternativa):
        saldo_alternativo = round(saldo_atual * random.uniform(0.5, 3.0), 2)
        self.cenarios.append({"realidade": "atual", "saldo": saldo_atual, "alternativa": decisao_alternativa, "saldo_alternativo": saldo_alternativo})
        return {"ok": True, "saldo_atual": saldo_atual, "saldo_na_outra_realidade": saldo_alternativo, "mensagem": f"Se você tivesse {decisao_alternativa}, hoje teria R$ {saldo_alternativo:,.2f}"}
print("✅ UBC MULTIVERSE pronto")
