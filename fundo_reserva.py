#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   FUNDO DE RESERVA TWS                   ║
║   Lastro real para UBC                   ║
╚══════════════════════════════════════════╝
"""
import json, os

class FundoReserva:
    def __init__(self):
        self.reserva_xmr = 0
        self.ubc_emitido = 0
        self.carregar()
    
    def carregar(self):
        if os.path.exists('reserva.json'):
            with open('reserva.json') as f:
                d = json.load(f)
                self.reserva_xmr = d.get('xmr', 0)
                self.ubc_emitido = d.get('ubc', 0)
    
    def salvar(self):
        with open('reserva.json', 'w') as f:
            json.dump({'xmr': self.reserva_xmr, 'ubc': self.ubc_emitido}, f, indent=2)
    
    def lastro(self):
        if self.ubc_emitido == 0: return 100
        return round((self.reserva_xmr / self.ubc_emitido) * 100, 2)
    
    def depositar_xmr(self, valor):
        self.reserva_xmr += valor
        self.salvar()
        return {"ok": True, "reserva_xmr": self.reserva_xmr, "lastro": f"{self.lastro()}%"}
    
    def emitir_ubc(self, valor):
        if self.reserva_xmr < valor: return {"erro": "Reserva insuficiente"}
        self.ubc_emitido += valor
        self.salvar()
        return {"ok": True, "ubc_emitido": self.ubc_emitido, "lastro": f"{self.lastro()}%"}

print("✅ Fundo de Reserva pronto")
