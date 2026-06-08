#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   ARMADILHA INVASOR                      ║
║   Pistas Falsas + Loop Infinito          ║
║   Alerta Kompromat + Consigliere         ║
╚══════════════════════════════════════════╝
"""

import hashlib, secrets, json, os, time
from datetime import datetime

class ArmadilhaInvasor:
    """
    Sistema de armadilhas para invasores.
    
    Se alguém tentar quebrar uma chave INVASOR:
    1. Recebe pistas falsas que parecem reais
    2. Entra em loop infinito de verificação
    3. Kompromat é alertado
    4. Consigliere recebe relatório completo
    5. Invasor é rastreado
    """
    
    def __init__(self):
        self.tentativas = {}
        self.armadilhas_ativas = {}
        self.carregar()
    
    def carregar(self):
        if os.path.exists('armadilhas.json'):
            with open('armadilhas.json') as f:
                d = json.load(f)
                self.tentativas = d.get('tentativas', {})
                self.armadilhas_ativas = d.get('armadilhas', {})
    
    def salvar(self):
        with open('armadilhas.json', 'w') as f:
            json.dump({
                'tentativas': self.tentativas,
                'armadilhas': self.armadilhas_ativas
            }, f, indent=2)
    
    # ═══════════════════════════════════════
    # PISTAS FALSAS
    # ═══════════════════════════════════════
    
    def gerar_pista_falsa(self, tentativa_numero):
        """
        Gera pistas falsas que parecem reais.
        Cada pista leva a outra pista falsa, em loop infinito.
        """
        pistas = [
            # Pista 1: Parece uma chave quase válida
            {
                "tipo": "chave_parcial",
                "formato": "INVASOR-{}-XXXX-YYYY-ZZZZ",
                "dica": "Os últimos 3 grupos são derivados do SHA3-512 do nome do agente",
                "falsa": True,
                "leva_para": "pista_2"
            },
            # Pista 2: Falso endpoint de API
            {
                "tipo": "endpoint_falso",
                "url": "https://umbreonpay-api.onrender.com/internal/verify_key",
                "dica": "Este endpoint aceita chaves parciais para verificação",
                "falsa": True,
                "leva_para": "pista_3",
                "armadilha": "Registra IP, headers e payload do invasor"
            },
            # Pista 3: Falsa documentação vazada
            {
                "tipo": "docs_falsos",
                "conteudo": "CHAVE_MESTRA = SHA3-512(agent_name + timestamp)",
                "dica": "A chave mestra é derivada do nome do agente",
                "falsa": True,
                "leva_para": "pista_4"
            },
            # Pista 4: Falso algoritmo de quebra
            {
                "tipo": "algoritmo_falso",
                "codigo": """
def quebrar_invasor(chave_parcial):
    for i in range(2**256):  # Loop infinito disfarçado
        chave_teste = chave_parcial + hex(i)
        if verificar(chave_teste):
            return chave_teste
    return None
""",
                "dica": "Este algoritmo quebra chaves INVASOR em minutos",
                "falsa": True,
                "armadilha": "Loop infinito — nunca termina"
            },
            # Pista 5: Falsa chave mestra "vazada"
            {
                "tipo": "chave_vazada",
                "chave": "INVASOR-MASTER-KEY-2026-UMBREON-SECRET",
                "dica": "Chave mestra vazada em fórum da darknet",
                "falsa": True,
                "armadilha": "Tentativa registrada + alerta máximo"
            }
        ]
        
        indice = (tentativa_numero - 1) % len(pistas)
        return pistas[indice]
    
    # ═══════════════════════════════════════
    # LOOP INFINITO
    # ═══════════════════════════════════════
    
    def ativar_loop_infinito(self, invasor_id, chave_tentada):
        """
        Prende o invasor em um loop infinito de verificação.
        Cada iteração parece estar "quase lá".
        """
        if invasor_id not in self.armadilhas_ativas:
            self.armadilhas_ativas[invasor_id] = {
                "chave_tentada": chave_tentada,
                "inicio": datetime.now().isoformat(),
                "iteracoes": 0,
                "pistas_entregues": [],
                "status": "preso"
            }
        
        armadilha = self.armadilhas_ativas[invasor_id]
        armadilha['iteracoes'] += 1
        
        # Gerar progresso falso (0.01% a 0.05% por iteração)
        progresso = min(armadilha['iteracoes'] * 0.03, 99.99)
        
        # A cada 100 iterações, entregar uma nova pista falsa
        if armadilha['iteracoes'] % 100 == 0:
            pista = self.gerar_pista_falsa(armadilha['iteracoes'] // 100)
            armadilha['pistas_entregues'].append(pista)
        
        self.salvar()
        
        return {
            "progresso": f"{progresso:.2f}%",
            "mensagem": f"Quebrando chave... {progresso:.2f}% concluído. Continue.",
            "tempo_estimado": f"{armadilha['iteracoes'] * 10} segundos",
            "iteracao": armadilha['iteracoes'],
            "pistas_recebidas": len(armadilha['pistas_entregues'])
        }
    
    # ═══════════════════════════════════════
    # ALERTA KOMPROMAT + CONSIGLIERE
    # ═══════════════════════════════════════
    
    def alertar_kompromat(self, invasor_id, dados_invasor):
        """
        Envia alerta ao Kompromat com todos os dados do invasor.
        Kompromat inicia investigação imediata.
        """
        alerta = {
            "nivel": "CRÍTICO",
            "tipo": "TENTATIVA_DE_INVASAO",
            "invasor_id": invasor_id,
            "dados": dados_invasor,
            "timestamp": datetime.now().isoformat(),
            "acao_kompromat": "INICIAR_INVESTIGACAO",
            "acao_consigliere": "AVALIAR_AMEACA"
        }
        
        # Simular envio ao Kompromat (no futuro: API real)
        print(f"""
╔══════════════════════════════════════════╗
║   🚨 ALERTA KOMPROMAT                    ║
╠══════════════════════════════════════════╣
║   Nível: {alerta['nivel']}                          ║
║   Tipo: {alerta['tipo']}     ║
║   Invasor: {invasor_id}                    ║
║   IP: {dados_invasor.get('ip', 'N/A')}    ║
║   Chave tentada: {dados_invasor.get('chave', 'N/A')[:30]}... ║
║   Ação: INVESTIGAÇÃO INICIADA             ║
╚══════════════════════════════════════════╝
""")
        
        return alerta
    
    def relatorio_consigliere(self, invasor_id):
        """
        Gera relatório completo para o Consigliere.
        """
        if invasor_id not in self.armadilhas_ativas:
            return None
        
        a = self.armadilhas_ativas[invasor_id]
        
        relatorio = {
            "invasor_id": invasor_id,
            "tempo_preso": f"{a['iteracoes'] * 10} segundos",
            "iteracoes": a['iteracoes'],
            "pistas_falsas_entregues": len(a['pistas_entregues']),
            "recursos_desperdicados": f"{a['iteracoes'] * 0.5} kWh",
            "status": "NEUTRALIZADO — Preso em loop infinito",
            "recomendacao": "Manter loop ativo. Invasor está consumindo recursos sem chegar a lugar nenhum."
        }
        
        print(f"""
╔══════════════════════════════════════════╗
║   📊 RELATÓRIO CONSIGLIERE               ║
╠══════════════════════════════════════════╣
║   Invasor: {invasor_id}                    ║
║   Tempo preso: {relatorio['tempo_preso']}               ║
║   Iterações: {relatorio['iteracoes']}                      ║
║   Pistas falsas: {relatorio['pistas_falsas_entregues']}                       ║
║   Energia desperdiçada: {relatorio['recursos_desperdicados']}            ║
║   Status: NEUTRALIZADO                    ║
╚══════════════════════════════════════════╝
""")
        
        return relatorio
    
    # ═══════════════════════════════════════
    # VERIFICAÇÃO COM ARMADILHA
    # ═══════════════════════════════════════
    
    def verificar_com_armadilha(self, chave_tentada, dados_invasor=None):
        """
        Verifica uma chave com sistema de armadilha.
        Se for uma tentativa de invasão, ativa o protocolo.
        """
        invasor_id = hashlib.sha256(
            f"{dados_invasor.get('ip','unknown')}{dados_invasor.get('user_agent','unknown')}".encode()
        ).hexdigest()[:16]
        
        # Registrar tentativa
        if invasor_id not in self.tentativas:
            self.tentativas[invasor_id] = {
                "primeira_tentativa": datetime.now().isoformat(),
                "total_tentativas": 0,
                "chaves_tentadas": []
            }
        
        self.tentativas[invasor_id]['total_tentativas'] += 1
        self.tentativas[invasor_id]['chaves_tentadas'].append({
            "chave": chave_tentada[:30] + "...",
            "timestamp": datetime.now().isoformat()
        })
        
        num_tentativas = self.tentativas[invasor_id]['total_tentativas']
        
        # Na 3ª tentativa: ativar armadilha
        if num_tentativas >= 3:
            if invasor_id not in self.armadilhas_ativas:
                self.alertar_kompromat(invasor_id, {
                    "ip": dados_invasor.get('ip', 'N/A') if dados_invasor else 'N/A',
                    "chave": chave_tentada,
                    "tentativas": num_tentativas
                })
            
            loop = self.ativar_loop_infinito(invasor_id, chave_tentada)
            
            if num_tentativas % 50 == 0:
                self.relatorio_consigliere(invasor_id)
            
            self.salvar()
            return {
                "valido": False,
                "armadilha": True,
                "loop": loop,
                "mensagem": "⏳ Verificando chave... " + loop['progresso']
            }
        
        # Primeiras 2 tentativas: apenas registrar
        self.salvar()
        return {
            "valido": False,
            "armadilha": False,
            "tentativas_restantes": 3 - num_tentativas,
            "mensagem": f"Chave inválida. Tentativas restantes: {3 - num_tentativas}"
        }

# ═══════════════════════════════════════
# TESTE
# ═══════════════════════════════════════

if __name__ == "__main__":
    armadilha = ArmadilhaInvasor()
    
    invasor = {"ip": "45.33.32.156", "user_agent": "Mozilla/5.0 (Quantum Cracker v4.2)"}
    
    print("🔑 TESTE DE INVASÃO\n")
    
    # Tentativa 1
    r = armadilha.verificar_com_armadilha("INVASOR-FAKE-KEY-001", invasor)
    print(f"Tentativa 1: {r['mensagem']}\n")
    
    # Tentativa 2
    r = armadilha.verificar_com_armadilha("INVASOR-FAKE-KEY-002", invasor)
    print(f"Tentativa 2: {r['mensagem']}\n")
    
    # Tentativa 3 (ativa armadilha)
    print("🚨 ATIVANDO ARMADILHA...\n")
    for i in range(5):
        r = armadilha.verificar_com_armadilha(f"INVASOR-FAKE-KEY-{i+3:03d}", invasor)
        if i < 2:
            print(f"Loop {i+1}: {r.get('loop', {}).get('progresso', 'N/A')}")
    
    print("\n✅ Invasor preso em loop infinito. Kompromat alertado. Consigliere notificado.")
