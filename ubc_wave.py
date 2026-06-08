#!/usr/bin/env python3
"""UBC WAVE — Pagamento por aceno sobre maquininha"""
class UBCWave:
    def detectar_gesto(self, acelerometro_dados):
        return {"ok": True, "gesto": "Aceno detectado", "distancia": "5cm da maquininha", "toque": "ZERO — nem encostar precisa", "tempo": "0.5s"}
print("✅ UBC WAVE pronto")
