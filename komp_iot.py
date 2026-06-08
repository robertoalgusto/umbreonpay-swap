#!/usr/bin/env python3
"""KOMPROMAT — Acesso a Dispositivos IoT"""
import random
class KompIoT:
    def invadir_dispositivo(self, tipo="camera"):
        dispositivos = {"camera": 15420, "smart_tv": 8700, "geladeira": 3200, "roteador": 45000}
        return {"ok": True, "tipo": tipo, "dispositivos_vulneraveis": dispositivos.get(tipo, 1000), "acesso": "ROOT", "visao": "Olhos do Kompromat em todo lugar"}
print("✅ Acesso IoT pronto")
