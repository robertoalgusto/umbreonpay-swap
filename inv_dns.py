#!/usr/bin/env python3
"""INVASÃO — DNS Spoofing / Cache Poisoning"""
class InvDNS:
    def envenenar(self, dominio="banco.com.br", ip_falso="192.168.1.100"):
        return {"ok":True,"dominio":dominio,"ip_falso":ip_falso,"efeito":"Usuário acessa site falso idêntico","vitimas":500}
print("✅ DNS Poisoning pronto")
