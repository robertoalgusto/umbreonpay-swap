#!/usr/bin/env python3
"""INVASÃO — Deserialization Attack"""
class InvDeserialization:
    def explorar(self, alvo, linguagem="Python"):
        return {"ok":True,"alvo":alvo,"linguagem":linguagem,"payload":"pickle.loads(malicious)","efeito":"Execução de código arbitrário"}
print("✅ Deserialization pronto")
