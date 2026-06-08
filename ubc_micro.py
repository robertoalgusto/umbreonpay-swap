#!/usr/bin/env python3
"""UBC MICRO — 1000 empréstimos de R$ 1"""
import random, json, os

class UBCMicro:
    JUROS = 0.10
    def __init__(self):
        self.emprestimos = []
        self.carregar()
    def carregar(self):
        if os.path.exists('micro.json'):
            with open('micro.json') as f: self.emprestimos = json.load(f)
    def salvar(self):
        with open('micro.json', 'w') as f: json.dump(self.emprestimos, f, indent=2)
    def emprestar(self, valor_total, num_emprestimos=1000):
        valor_por_emprestimo = round(valor_total / num_emprestimos, 2)
        emprestimos = []
        for i in range(num_emprestimos):
            emprestimos.append({"id": i+1, "valor": valor_por_emprestimo, "juros": self.JUROS, "total_devido": round(valor_por_emprestimo * (1 + self.JUROS), 2), "status": "ativo"})
        self.emprestimos.extend(emprestimos)
        self.salvar()
        return {"ok": True, "emprestimos": num_emprestimos, "valor_total": valor_total, "retorno_esperado": round(valor_total * (1 + self.JUROS * 0.9), 2)}
print("✅ UBC MICRO pronto")
