#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   MODO FANTASMA                          ║
║   App se disfarça de calculadora         ║
╚══════════════════════════════════════════╝
"""
import json, os

class ModoFantasma:
    def __init__(self):
        self.config = {"modo_fantasma": False, "disfarce": "calculadora", "pacote_falso": "com.calculadora.basica"}
        self.carregar()
    
    def carregar(self):
        if os.path.exists('fantasma.json'):
            with open('fantasma.json') as f:
                self.config = json.load(f)
    
    def salvar(self):
        with open('fantasma.json', 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def ativar(self):
        """Ativa o modo fantasma — app vira calculadora"""
        self.config['modo_fantasma'] = True
        self.salvar()
        return {"modo": "FANTASMA ATIVADO", "aparencia": "Calculadora", "acesso_real": "Digite 9999 para abrir o app real"}
    
    def desativar(self, codigo):
        """Desativa o modo fantasma com código secreto"""
        if codigo == "9999":
            self.config['modo_fantasma'] = False
            self.salvar()
            return {"modo": "FANTASMA DESATIVADO", "aparencia": "UmbreonPay"}
        return {"erro": "Código incorreto"}

print("✅ Modo Fantasma pronto")
