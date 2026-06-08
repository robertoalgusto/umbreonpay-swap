#!/usr/bin/env python3
"""INVASÃO — Server-Side Request Forgery (SSRF)"""
class InvSSRF:
    def explorar(self, servidor, endpoint_interno="http://169.254.169.254/latest/meta-data/"):
        return {"ok": True, "servidor": servidor, "acesso_interno": endpoint_interno, "dados_obtidos": "Credenciais AWS, chaves API, tokens de acesso"}
print("✅ SSRF pronto")
