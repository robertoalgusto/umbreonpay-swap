#!/usr/bin/env python3
"""UBC DEAD DROP — Transferência por coordenada GPS"""
import secrets
class UBCDeadDrop:
    def __init__(self):
        self.drops = {}
    def criar(self, valor, lat, lon, raio_metros=10):
        drop_id = secrets.token_hex(8)
        self.drops[drop_id] = {"valor": valor, "lat": lat, "lon": lon, "raio": raio_metros, "status": "disponivel"}
        return {"ok": True, "id": drop_id, "instrucao": f"Vá até ({lat}, {lon}) para resgatar {valor} UBC"}
    def resgatar(self, drop_id, lat_atual, lon_atual):
        if drop_id not in self.drops: return {"erro": "Drop não encontrado"}
        d = self.drops[drop_id]
        distancia = ((lat_atual - d['lat'])**2 + (lon_atual - d['lon'])**2)**0.5 * 111000
        if distancia <= d['raio']:
            d['status'] = 'resgatado'
            return {"ok": True, "valor": d['valor']}
        return {"erro": f"Você está a {round(distancia,1)}m do ponto. Chegue mais perto."}
print("✅ UBC DEAD DROP pronto")
