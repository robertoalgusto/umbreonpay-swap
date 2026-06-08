#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   TEMA + WIDGET                          ║
║   Dark/Light Mode + Saldo na tela       ║
╚══════════════════════════════════════════╝
"""
import json, os

class TemaWidget:
    TEMAS = {"dark": {"bg": "#0A0A0A", "texto": "#FFF", "destaque": "#C9A84C"},
             "light": {"bg": "#FFF", "texto": "#0A0A0A", "destaque": "#8B7500"},
             "high_contrast": {"bg": "#000", "texto": "#FFF", "destaque": "#FFD600"}}
    
    def __init__(self):
        self.config = {"tema": "dark", "widget_ativo": False, "widget_mostrar": "saldo"}
        self.carregar()
    
    def carregar(self):
        if os.path.exists('tema.json'):
            with open('tema.json') as f:
                self.config = json.load(f)
    
    def salvar(self):
        with open('tema.json', 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def mudar_tema(self, tema):
        if tema in self.TEMAS:
            self.config['tema'] = tema
            self.salvar()
            return {"ok": True, "tema": tema, "cores": self.TEMAS[tema]}
        return {"erro": "Tema inválido"}
    
    def ativar_widget(self):
        self.config['widget_ativo'] = True
        self.salvar()
        return {"widget": "ATIVADO", "tela_inicial": "Saldo UBC visível"}

print("✅ Tema + Widget pronto")
