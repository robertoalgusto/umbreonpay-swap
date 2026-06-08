#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   PUSH NOTIFICATIONS                     ║
║   Alertas em tempo real                  ║
╚══════════════════════════════════════════╝
"""
import json, os
from datetime import datetime

class PushNotifications:
    def __init__(self):
        self.inscritos = {}
        self.notificacoes = []
        self.carregar()
    
    def carregar(self):
        if os.path.exists('push.json'):
            with open('push.json') as f:
                d = json.load(f)
                self.inscritos = d.get('inscritos', {})
                self.notificacoes = d.get('notificacoes', [])
    
    def salvar(self):
        with open('push.json', 'w') as f:
            json.dump({'inscritos': self.inscritos, 'notificacoes': self.notificacoes}, f, indent=2)
    
    def inscrever(self, usuario, token):
        self.inscritos[usuario] = {"token": token, "ativo": True}
        self.salvar()
        return {"ok": True}
    
    def enviar(self, usuario, titulo, mensagem):
        if usuario in self.inscritos:
            notif = {"usuario": usuario, "titulo": titulo, "mensagem": mensagem, "data": datetime.now().isoformat(), "lida": False}
            self.notificacoes.append(notif)
            self.salvar()
            return {"ok": True, "enviado": True}
        return {"erro": "Usuário não inscrito"}
    
    def nao_lidas(self, usuario):
        return [n for n in self.notificacoes if n['usuario'] == usuario and not n['lida']]

print("✅ Push Notifications pronto")
