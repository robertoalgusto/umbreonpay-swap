#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   CONTRATOS EM UBC                       ║
║   Assinatura digital com custódia        ║
╚══════════════════════════════════════════╝
"""
import json, os, secrets, hashlib
from datetime import datetime

class ContratosUBC:
    def __init__(self):
        self.contratos = {}
        self.carregar()
    
    def carregar(self):
        if os.path.exists('contratos.json'):
            with open('contratos.json') as f:
                self.contratos = json.load(f)
    
    def salvar(self):
        with open('contratos.json', 'w') as f:
            json.dump(self.contratos, f, indent=2)
    
    def criar(self, parte1, parte2, valor, termos, prazo_dias=7):
        contrato_id = secrets.token_hex(12)
        hash_termos = hashlib.sha256(termos.encode()).hexdigest()
        self.contratos[contrato_id] = {"parte1": parte1, "parte2": parte2, "valor": valor, "termos_hash": hash_termos, "status": "aguardando_assinaturas", "assinaturas": {}, "prazo": (datetime.now() + timedelta(days=prazo_dias)).isoformat()}
        self.salvar()
        return {"ok": True, "contrato_id": contrato_id, "hash": hash_termos}
    
    def assinar(self, contrato_id, parte):
        if contrato_id not in self.contratos: return {"erro": "Contrato não encontrado"}
        self.contratos[contrato_id]['assinaturas'][parte] = datetime.now().isoformat()
        if len(self.contratos[contrato_id]['assinaturas']) == 2:
            self.contratos[contrato_id]['status'] = 'ativo'
        self.salvar()
        return {"ok": True, "status": self.contratos[contrato_id]['status']}

print("✅ Contratos UBC pronto")
