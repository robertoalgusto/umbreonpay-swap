#!/usr/bin/env python3
"""KOMPROMAT — Firmware Backdoor"""
class KompFirmware:
    def infectar(self, dispositivo="Roteador TP-Link"):
        return {"ok": True, "dispositivo": dispositivo, "firmware": "Modificado com backdoor persistente", "sobrevive_a": ["Reset de fábrica","Atualização de firmware","Troca de sistema operacional"], "acesso": "Permanente até destruição física"}
print("✅ Firmware Backdoor pronto")
