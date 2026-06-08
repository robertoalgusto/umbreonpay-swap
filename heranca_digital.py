#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   HERANÇA DIGITAL AUTOMÁTICA             ║
║   UBC transferido após inatividade       ║
╚══════════════════════════════════════════╝
"""
import json, os
from datetime import datetime, timedelta

class HerancaDigital:
    MESES_INATIVIDADE = 12
    
    def __init__(self):
        self.herancas = {}
        self.carregar()
    
    def carregar(self):
        if os.path.exists('herancas.json'):
            with open('herancas.json') as f:
                self.herancas = json.load(f)
    
    def salvar(self):
        with open('herancas.json', 'w') as f:
            json.dump(self.herancas, f, indent=2)
    
    def configurar(self, carteira_origem, carteira_herdeiro, meses=MESES_INATIVIDADE):
        self.herancas[carteira_origem] = {"herdeiro": carteira_herdeiro, "meses": meses, "ultimo_login": datetime.now().isoformat(), "status": "ativo"}
        self.salvar()
        return {"ok": True, "mensagem": f"Herança configurada. Após {meses} meses de inatividade, saldo vai para {carteira_herdeiro[:20]}..."}
    
    def registrar_login(self, carteira):
        if carteira in self.herancas:
            self.herancas[carteira]['ultimo_login'] = datetime.now().isoformat()
            self.salvar()
    
    def verificar(self):
        transferencias = []
        for origem, h in list(self.herancas.items()):
            if h['status'] == 'ativo':
                ultimo = datetime.fromisoformat(h['ultimo_login'])
                if datetime.now() - ultimo > timedelta(days=h['meses'] * 30):
                    h['status'] = 'transferido'
                    transferencias.append({"origem": origem, "herdeiro": h['herdeiro']})
        self.salvar()
        return {"ok": True, "transferencias": transferencias}

print("✅ Herança Digital pronta")
