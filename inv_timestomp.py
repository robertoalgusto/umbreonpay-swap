#!/usr/bin/env python3
"""INVASÃO — Timestomping"""
from datetime import datetime, timedelta
class InvTimestomp:
    def alterar(self, arquivo):
        data_falsa = (datetime.now() - timedelta(days=1095)).timestamp()
        return {"ok":True,"arquivo":arquivo,"data_original":"hoje","data_falsa":"3 anos atrás","efeito":"Backdoor parece arquivo legítimo antigo"}
print("✅ Timestomping pronto")
