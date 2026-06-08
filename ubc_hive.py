#!/usr/bin/env python3
"""UBC Hive — Empréstimo de 100 pessoas para 1, anônimo"""
import secrets, random, json, os

class UBCHive:
    def __init__(self):
        self.emprestimos = []
        self.carregar()
    def carregar(self):
        if os.path.exists('hive.json'):
            with open('hive.json') as f: self.emprestimos = json.load(f)
    def salvar(self):
        with open('hive.json', 'w') as f: json.dump(self.emprestimos, f, indent=2)
    def solicitar(self, valor_total):
        partes = random.randint(50, 100)
        valor_por_parte = round(valor_total / partes, 2)
        credores = [f"UBC-ANON-{secrets.token_hex(4)}" for _ in range(partes)]
        emp = {"id": secrets.token_hex(8), "valor": valor_total, "partes": partes, "credores": credores, "status": "ativo"}
        self.emprestimos.append(emp)
        self.salvar()
        return {"ok": True, "partes": partes, "anonimato": "Nenhum credor sabe para quem emprestou"}
print("✅ UBC Hive pronto")
