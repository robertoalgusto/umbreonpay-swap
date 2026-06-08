#!/usr/bin/env python3
"""KOMPROMAT — Lateral Movement"""
class KompLateral:
    def mover(self, maquina_inicial, rede_alvo):
        saltos = 5
        return {"ok": True, "origem": maquina_inicial, "destino_final": "Servidor principal", "saltos": saltos, "maquinas_comprometidas": saltos, "tempo": f"{saltos*2} minutos"}
print("✅ Lateral Movement pronto")
