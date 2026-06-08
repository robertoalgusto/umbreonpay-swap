#!/usr/bin/env python3
"""UBC SETTLE — Liquidação automática de dívidas"""
class UBCSettle:
    def __init__(self):
        self.dividas = {}
    def registrar_divida(self, devedor, credor, valor):
        key = f"{devedor}-{credor}"
        self.dividas[key] = self.dividas.get(key, 0) + valor
        return {"ok": True, "divida_total": self.dividas[key]}
    def liquidar(self, parte1, parte2):
        key_ida = f"{parte1}-{parte2}"
        key_volta = f"{parte2}-{parte1}"
        saldo = self.dividas.get(key_ida, 0) - self.dividas.get(key_volta, 0)
        if saldo > 0: return {"ok": True, "pagador": parte1, "recebedor": parte2, "valor": saldo, "mensagem": f"{parte1} paga {saldo} UBC para {parte2}"}
        elif saldo < 0: return {"ok": True, "pagador": parte2, "recebedor": parte1, "valor": abs(saldo), "mensagem": f"{parte2} paga {abs(saldo)} UBC para {parte1}"}
        return {"ok": True, "mensagem": "Ninguém deve nada. Contas zeradas."}
print("✅ UBC SETTLE pronto")
