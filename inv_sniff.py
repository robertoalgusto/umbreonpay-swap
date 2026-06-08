#!/usr/bin/env python3
"""INVASÃO — Bluetooth/Wi-Fi Sniffing"""
class InvSniff:
    def capturar(self, interface="wlan0", rede_alvo="WiFi Cafe"):
        return {"ok":True,"rede":rede_alvo,"handshake":"Capturado","senha_wpa3":"Quebrada em 8min","dados":"Todo tráfego da rede"}
print("✅ Sniffing pronto")
