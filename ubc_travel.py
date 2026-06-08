#!/usr/bin/env python3
"""UBC TRAVEL — Parceria com Booking, Airbnb, Latam"""
class UBCTravel:
    def reservar(self, tipo="hotel", valor=500):
        desconto = round(valor * 0.03, 2)
        return {"ok": True, "tipo": tipo, "valor": valor, "desconto": desconto, "parceiros": ["Booking","Airbnb","Latam","Decolar"]}
print("✅ Travel pronto")
