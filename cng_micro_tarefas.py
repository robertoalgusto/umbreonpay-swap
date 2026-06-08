#!/usr/bin/env python3
"""CNG MICRO TAREFAS — Trabalhos automáticos em plataformas"""
import random
class CNGMicroTarefas:
    PLATAFORMAS = ["Amazon MTurk", "Appen", "Clickworker", "Remotasks", "Testable Minds"]
    def __init__(self):
        self.ganho_total = 0
        self.tarefas = 0
    def executar_tarefa(self):
        plataforma = random.choice(self.PLATAFORMAS)
        ganho = round(random.uniform(0.50, 5.00), 2)
        self.ganho_total += ganho
        self.tarefas += 1
        return {"ok": True, "plataforma": plataforma, "ganho": ganho, "total": self.ganho_total, "tarefas": self.tarefas}
print("✅ CNG Micro Tarefas pronto")
