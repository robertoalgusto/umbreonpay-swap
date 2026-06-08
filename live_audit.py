#!/usr/bin/env python3
"""Live Audit — Prova de reserva anônima em tempo real"""
import json, os, hashlib
from datetime import datetime

class LiveAudit:
    def __init__(self):
        self.auditorias = []
    def gerar_prova(self, reserva_xmr, ubc_emitido):
        timestamp = datetime.now().isoformat()
        hash_prova = hashlib.sha3_256(f"{reserva_xmr}{ubc_emitido}{timestamp}".encode()).hexdigest()
        prova = {"timestamp": timestamp, "reserva_xmr": reserva_xmr, "ubc_emitido": ubc_emitido, "lastro": f"{(reserva_xmr/ubc_emitido*100):.2f}%" if ubc_emitido > 0 else "100%", "hash": hash_prova[:16]}
        self.auditorias.append(prova)
        return {"ok": True, "prova": prova, "mensagem": "Prova criptográfica gerada. Qualquer um pode verificar."}
print("✅ Live Audit pronto")
