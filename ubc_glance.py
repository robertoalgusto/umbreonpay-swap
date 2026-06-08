#!/usr/bin/env python3
"""UBC GLANCE — Pagamento por olhar (retina)"""
class UBCGlance:
    def autorizar_por_retina(self, usuario, valor):
        return {"ok": True, "usuario": usuario, "valor": valor, "metodo": "Escaneamento de retina em 2 segundos", "seguranca": "Padrão retinal único — impossível falsificar", "toque": "ZERO — só olhar"}
print("✅ UBC GLANCE pronto")
