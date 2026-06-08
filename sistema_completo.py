#!/usr/bin/env python3
import hashlib, secrets, json, os, base64
from datetime import datetime, timedelta
from chave_invasor import ChaveInvasor
from armadilha_invasor import ArmadilhaInvasor

class UmbreonPay:
    def __init__(self):
        self.carteiras = {}
        self.agentes = {}
        self.chaves_invasor = {}
        self.transacoes = []
        self.armadilha = ArmadilhaInvasor()
        self.carregar()
    
    def carregar(self):
        if os.path.exists('sistema.json'):
            with open('sistema.json') as f:
                d = json.load(f)
                self.carteiras = d.get('carteiras', {})
                self.agentes = d.get('agentes', {})
                self.chaves_invasor = d.get('chaves_invasor', {})
                self.transacoes = d.get('transacoes', [])
    
    def salvar(self):
        with open('sistema.json', 'w') as f:
            json.dump({
                'carteiras': self.carteiras, 'agentes': self.agentes,
                'chaves_invasor': self.chaves_invasor, 'transacoes': self.transacoes
            }, f, indent=2)
    
    def criar_agente_invasor(self, nome, nivel=3):
        par = ChaveInvasor.gerar_par_agente(nome, nivel)
        agente_id = f"AG-{secrets.token_hex(4).upper()}"
        self.agentes[agente_id] = {
            "nome": nome, "nivel": nivel,
            "hash_invasor": par['hash_armazenado'],
            "codigo_visivel": par['codigo_visivel'],
            "taxa_pix": 0, "taxa_saque": 0, "taxa_swap": 0, "taxa_nfc": 0,
            "status": "ativo"
        }
        self.chaves_invasor[par['hash_armazenado']] = agente_id
        self.salvar()
        return {"agente_id": agente_id, "chave_invasor": par['chave_invasor'], "codigo_visivel": par['codigo_visivel']}
    
    def verificar_invasor(self, chave_invasor):
        hash_chave = ChaveInvasor.hash_para_armazenamento(chave_invasor)
        for hash_guardado, agente_id in self.chaves_invasor.items():
            if secrets.compare_digest(hash_chave, hash_guardado):
                if self.agentes[agente_id]['status'] == 'ativo':
                    return agente_id
        return None
    
    def verificar_com_armadilha(self, chave_tentada, dados_invasor=None):
        """Verifica chave com sistema de armadilha"""
        # Primeiro verifica se é válida
        agente_id = self.verificar_invasor(chave_tentada)
        if agente_id:
            return {"valido": True, "agente_id": agente_id}
        
        # Se não for, ativa armadilha
        return self.armadilha.verificar_com_armadilha(chave_tentada, dados_invasor)
    
    def calcular_taxa(self, valor, tipo, chave_invasor=None):
        if chave_invasor and self.verificar_invasor(chave_invasor):
            return 0
        taxas = {"pix": 0.25, "saque": 0.15, "swap": 0.005, "nfc": 0}
        return round(valor * taxas.get(tipo, 0), 2)
    
    def criar_carteira(self, titular="anon"):
        endereco = "UBC-" + secrets.token_hex(32)
        self.carteiras[endereco] = {"titular": titular, "saldo_ubc": 0, "tipo": "usuario", "criada_em": datetime.now().isoformat()}
        self.salvar()
        return {"endereco": endereco, "titular": titular}
    
    def pagar_pix(self, carteira, valor_brl, chave_invasor=None):
        if carteira not in self.carteiras: return {"erro": "Carteira não encontrada"}
        valor_ubc = valor_brl / 1200
        taxa = self.calcular_taxa(valor_brl, 'pix', chave_invasor)
        total_ubc = valor_ubc + (taxa / 1200)
        if self.carteiras[carteira]['saldo_ubc'] < total_ubc: return {"erro": "Saldo insuficiente"}
        self.carteiras[carteira]['saldo_ubc'] -= total_ubc
        tx = {"id": secrets.token_hex(8), "tipo": "pix", "valor_brl": valor_brl, "taxa": taxa, "invasor": "✅" if taxa == 0 else "❌"}
        self.transacoes.append(tx)
        self.salvar()
        return {"ok": True, "transacao": tx, "taxa": taxa}

# Teste
if __name__ == "__main__":
    sistema = UmbreonPay()
    agente = sistema.criar_agente_invasor("Agente Silva")
    print(f"🦅 Agente criado: {agente['agente_id']}")
    print(f"🔑 Chave INVASOR: {agente['chave_invasor'][:50]}...")
    
    # Testar chave falsa (aciona armadilha)
    print("\n🚨 Testando invasão...")
    for i in range(4):
        r = sistema.verificar_com_armadilha(f"CHAVE-FALSA-{i}", {"ip": "10.0.0.99"})
        if isinstance(r, dict):
            print(f"   {r.get('mensagem', 'N/A')}")
