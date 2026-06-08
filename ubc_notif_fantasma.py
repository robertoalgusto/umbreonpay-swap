#!/usr/bin/env python3
"""NOTIFICAÇÕES FANTASMA — Alertas disfarçados de sistema"""
class NotifFantasma:
    def disfarcar(self, mensagem_real="+R$ 500 recebido"):
        disfarces = ["Atualização do sistema disponível","Google Play Services","Hora de se hidratar 💧","Nova foto salva na galeria"]
        return {"ok": True, "mensagem_real": mensagem_real, "disfarce": __import__('random').choice(disfarces), "visivel_para": "Apenas o Don — outros veem notificação normal"}
print("✅ Notificações Fantasma pronto")
