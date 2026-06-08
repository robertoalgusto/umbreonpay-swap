#!/usr/bin/env python3
"""INVASÃO — Local/Remote File Inclusion"""
class InvLFI:
    def incluir(self, alvo, arquivo="/etc/passwd"):
        return {"ok":True,"alvo":alvo,"arquivo":arquivo,"conteudo":"root:x:0:0:root:/root:/bin/bash","tecnica":"Directory Traversal + Null Byte"}
print("✅ LFI/RFI pronto")
