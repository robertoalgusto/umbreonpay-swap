#!/usr/bin/env python3
"""UBC EMERGENCY FUND — Cálculo automático de reserva de emergência"""
class UBCEmergencyFund:
    def calcular(self, gastos_mensais):
        reserva_ideal = gastos_mensais * 6
        return {"ok": True, "gastos_mensais": gastos_mensais, "reserva_ideal": reserva_ideal, "plano": f"Guardar {round(reserva_ideal/12,2)} UBC/mês por 12 meses"}
print("✅ Emergency Fund pronto")
