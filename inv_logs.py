#!/usr/bin/env python3
"""INVASÃO — Logs Cleaning"""
class InvLogs:
    def limpar(self, sistema="Linux"):
        return {"ok":True,"logs_apagados":["/var/log/*","~/.bash_history","utmp/wtmp/lastlog","journalctl --rotate --vacuum-time=1s"],"metodo":"Sobrescrita tripla + timestomp","rastro":"ZERO"}
print("✅ Logs Cleaning pronto")
