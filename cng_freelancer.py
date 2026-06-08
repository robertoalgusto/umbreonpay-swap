#!/usr/bin/env python3
"""CNG FREELANCER — Trabalhos no Upwork/Fiverr"""
import random
class CNGFreelancer:
    PLATAFORMAS = ["Upwork", "Fiverr", "Workana", "99Freelas", "Freelancer.com"]
    HABILIDADES = ["Python", "Bot Telegram", "Web Scraping", "Automação", "API REST", "Script"]
    def __init__(self):
        self.trabalhos = 0
        self.ganho = 0
    def pegar_trabalho(self):
        plataforma = random.choice(self.PLATAFORMAS)
        habilidade = random.choice(self.HABILIDADES)
        valor = random.randint(50, 300)
        self.trabalhos += 1
        self.ganho += valor
        return {"ok": True, "plataforma": plataforma, "habilidade": habilidade, "valor": valor, "total": self.ganho}
print("✅ CNG Freelancer pronto")
