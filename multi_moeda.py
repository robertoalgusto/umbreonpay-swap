#!/usr/bin/env python3
class MultiMoeda:
    COT = {"BRL":1200,"USD":240,"EUR":220,"GBP":190,"JPY":36000,"CNY":1700,"INR":20000}
    SIM = {"BRL":"R$","USD":"$","EUR":"€","GBP":"£","JPY":"¥","CNY":"¥","INR":"₹"}
    @classmethod
    def converter(cls, v, origem, destino="XMR"):
        if destino=="XMR": return round(v/cls.COT.get(origem,1),6)
        return round(v*cls.COT.get(destino,1),2)
    @classmethod
    def formatar(cls, v, moeda):
        s = cls.SIM.get(moeda,"")
        if moeda in ["JPY","INR"]: return f"{s} {v:,.0f}"
        return f"{s} {v:,.2f}"
print("✅ Multi-Moeda pronto")
