#!/usr/bin/env python3
"""UBC ORACLE — Aposte contra si mesmo"""
class UBCOracle:
    def __init__(self):
        self.apostas = {}
    def apostar(self, usuario, meta, valor_aposta, prazo_dias=30):
        self.apostas[usuario] = {"meta": meta, "aposta": valor_aposta, "prazo": prazo_dias, "status": "ativa"}
        return {"ok": True, "mensagem": f"Se não cumprir '{meta}' em {prazo_dias} dias, perde {valor_aposta} UBC"}
    def verificar(self, usuario, cumpriu):
        if usuario not in self.apostas: return {"erro": "Aposta não encontrada"}
        a = self.apostas[usuario]
        a['status'] = 'encerrada'
        return {"ok": True, "resultado": "Ganhou a aposta" if cumpriu else f"Perdeu {a['aposta']} UBC", "medo_de_perder": "Maior que a vontade de ganhar"}
print("✅ UBC ORACLE pronto")
