#!/usr/bin/env python3
"""UBC GENOME — DNA como assinatura"""
import hashlib
class UBCGenome:
    def __init__(self):
        self.genomas = {}
    def registrar(self, usuario, sequencia_dna):
        self.genomas[usuario] = hashlib.sha3_512(sequencia_dna.encode()).hexdigest()
        return {"ok": True, "mensagem": "A senha está no seu sangue"}
    def verificar(self, usuario, sequencia):
        return {"autentico": hashlib.sha3_512(sequencia.encode()).hexdigest() == self.genomas.get(usuario, "")}
print("✅ UBC GENOME pronto")
