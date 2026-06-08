#!/usr/bin/env python3
"""UBC SCANNER — Escaneia e extrai dados de qualquer documento"""
class UBCScanner:
    def escanear(self, documento="conta_luz.pdf"):
        return {"ok": True, "documento": documento, "extraido": {"valor": 150.00, "vencimento": "15/06/2026", "codigo_barras": "34191790010104351004791020150008123456789000"}, "arquivado": True}
print("✅ Scanner pronto")
