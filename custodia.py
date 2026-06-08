#!/usr/bin/env python3
import secrets, json, os
from datetime import datetime

class CustodyContract:
    def __init__(self):
        self.contratos = []
        if os.path.exists("contratos.json"):
            with open("contratos.json") as f:
                self.contratos = json.load(f)
    def salvar(self):
        with open("contratos.json","w") as f:
            json.dump(self.contratos, f, indent=2)
    def criar(self, comprador, fornecedor, brl, xmr):
        c = {"id":"UB-SWAP-"+secrets.token_hex(6).upper(),"comprador":comprador,"fornecedor":fornecedor,"brl":brl,"xmr":xmr,"status":"aguardando","data":datetime.now().isoformat()}
        self.contratos.append(c)
        self.salvar()
        return c
print("✅ Custody pronto")
