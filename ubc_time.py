#!/usr/bin/env python3
"""UBC TIME — Tempo humano como lastro"""
import json, os
from datetime import datetime, timedelta
class UBCTime:
    UBC_POR_HORA = 1.0
    def __init__(self):
        self.trabalhos = {}
    def registrar_trabalho(self, usuario, horas, prova):
        self.trabalhos[usuario] = {"horas": self.trabalhos.get(usuario, {}).get('horas', 0) + horas, "ubc_ganho": horas * self.UBC_POR_HORA, "ultima_prova": prova}
        return {"ok": True, "horas_trabalhadas": horas, "ubc_emitido": horas * self.UBC_POR_HORA}
print("✅ UBC TIME pronto")
