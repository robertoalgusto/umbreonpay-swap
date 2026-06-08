#!/usr/bin/env python3
"""Geo Prova — Transação só autorizada em localização específica"""
import json, os

class GeoProva:
    def __init__(self):
        self.restricoes = {}
        self.carregar()
    def carregar(self):
        if os.path.exists('geo.json'):
            with open('geo.json') as f: self.restricoes = json.load(f)
    def salvar(self):
        with open('geo.json', 'w') as f: json.dump(self.restricoes, f, indent=2)
    def configurar(self, carteira, lat, lon, raio_metros=500):
        self.restricoes[carteira] = {"lat": lat, "lon": lon, "raio": raio_metros, "ativo": True}
        self.salvar()
        return {"ok": True, "mensagem": f"Transações só autorizadas em {raio_metros}m de ({lat}, {lon})"}
    def verificar(self, carteira, lat_atual, lon_atual):
        if carteira not in self.restricoes: return {"autorizado": True}
        r = self.restricoes[carteira]
        distancia = ((lat_atual - r['lat'])**2 + (lon_atual - r['lon'])**2)**0.5 * 111000
        return {"autorizado": distancia <= r['raio'], "distancia": round(distancia, 1)}
print("✅ Geo Prova pronto")
