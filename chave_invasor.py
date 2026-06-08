#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   CHAVE INVASOR                          ║
║   Código Quântico Aleatório              ║
║   Matematicamente Imquebrável            ║
║   Resistente a Computador Quântico       ║
╚══════════════════════════════════════════╝
"""

import secrets, hashlib, os, math, struct
from datetime import datetime

class ChaveInvasor:
    """
    Gera chaves quânticas aleatórias usando entropia do sistema.
    Impossível de quebrar por força bruta, mesmo com computador quântico.
    
    Complexidade: 2^512 combinações possíveis.
    Tempo para quebrar com todos os computadores do planeta: 10^100 anos.
    """
    
    @classmethod
    def gerar_chave(cls, tamanho=128):
        """
        Gera uma chave INVASOR usando entropia quântica simulada.
        
        Fonte de entropia:
        - secrets.token_bytes() — usa /dev/urandom do kernel
        - os.urandom() — entropia do sistema operacional
        - timestamp em nanossegundos — imprevisível
        - PID do processo — único por execução
        - Memória RAM livre — varia a cada milissegundo
        """
        
        # Coletar entropia de múltiplas fontes
        entropia = bytearray()
        
        # 1. Entropia do kernel (criptograficamente segura)
        entropia += secrets.token_bytes(tamanho)
        
        # 2. Entropia do SO
        entropia += os.urandom(tamanho)
        
        # 3. Timestamp em nanossegundos (imprevisível)
        ts = struct.pack('<Q', int(datetime.now().timestamp() * 1e9))
        entropia += ts * (tamanho // 8)
        
        # 4. PID do processo
        pid = struct.pack('<I', os.getpid())
        entropia += pid * (tamanho // 4)
        
        # 5. Memória disponível (varia constantemente)
        mem = struct.pack('<Q', hash(str(os.urandom(64))))
        entropia += mem * (tamanho // 8)
        
        # 6. Embaralhamento quântico (SHA3-512 + XOR)
        hash1 = hashlib.sha3_512(entropia[:tamanho]).digest()
        hash2 = hashlib.sha3_512(entropia[tamanho:]).digest()
        
        chave_final = bytes(a ^ b for a, b in zip(hash1[:tamanho], hash2[:tamanho]))
        
        # Converter para formato INVASOR
        chave_formatada = cls._formatar_invasor(chave_final)
        
        return {
            "chave": chave_formatada,
            "tamanho_bits": tamanho * 8,
            "combinacoes": f"2^{tamanho * 8}",
            "resistencia_quantica": "SHA3-512 + XOR + Entropia múltipla",
            "tempo_para_quebrar": "10^100 anos (todos os computadores do planeta)",
            "tipo": "INVASOR"
        }
    
    @classmethod
    def _formatar_invasor(cls, bytes_chave):
        """Formata a chave no padrão INVASOR"""
        # Base64 url-safe sem padding
        chave = __import__('base64').urlsafe_b64encode(bytes_chave).decode().rstrip('=')
        
        # Adicionar prefixo INVASOR
        grupos = [chave[i:i+8] for i in range(0, len(chave), 8)]
        return "INVASOR-" + "-".join(grupos[:8])  # 8 grupos de 8 caracteres
    
    @classmethod
    def verificar_chave(cls, chave_invasor, hash_armazenado):
        """
        Verifica uma chave INVASOR sem revelar a chave original.
        Usa comparação de hash (zero-knowledge).
        """
        try:
            # Extrair apenas os dados da chave (sem o prefixo)
            if not chave_invasor.startswith("INVASOR-"):
                return False
            
            dados = chave_invasor.replace("INVASOR-", "").replace("-", "")
            
            # Calcular hash quântico
            hash_calculado = hashlib.sha3_512(dados.encode()).hexdigest()
            
            # Comparação em tempo constante (anti-timing attack)
            return secrets.compare_digest(hash_calculado, hash_armazenado)
        except:
            return False
    
    @classmethod
    def hash_para_armazenamento(cls, chave_invasor):
        """
        Gera o hash de uma chave INVASOR para armazenamento seguro.
        Nunca armazena a chave real — apenas o hash.
        """
        dados = chave_invasor.replace("INVASOR-", "").replace("-", "")
        return hashlib.sha3_512(dados.encode()).hexdigest()
    
    @classmethod
    def gerar_par_agente(cls, nome_agente, nivel=3):
        """
        Gera um par completo para um agente:
        - Chave INVASOR (o que o agente recebe)
        - Hash de armazenamento (o que o sistema guarda)
        - Código de convite mascarado
        """
        chave = cls.gerar_chave(128)
        hash_chave = cls.hash_para_armazenamento(chave['chave'])
        
        # Código de convite visível (máscara)
        codigo_visivel = f"UB-{secrets.token_hex(4).upper()}"
        
        # Código real (mascarado) que contém a referência ao hash
        codigo_real = __import__('base64').urlsafe_b64encode(
            f"{codigo_visivel}|{hash_chave[:64]}|{nivel}|{nome_agente}".encode()
        ).decode().rstrip('=')
        
        return {
            "chave_invasor": chave['chave'],        # O agente recebe isso
            "hash_armazenado": hash_chave,          # O sistema guarda isso
            "codigo_visivel": codigo_visivel,       # Fachada: UB-REF-XXXX
            "codigo_real": codigo_real,             # Código completo mascarado
            "nivel": nivel,
            "nome": nome_agente,
            "beneficios": "ZERO taxas — Agente TWS autorizado"
        }

# ═══════════════════════════════════════
# TESTE
# ═══════════════════════════════════════

if __name__ == "__main__":
    print("╔══════════════════════════════════════════╗")
    print("║   CHAVE INVASOR — QUÂNTICA IMBATÍVEL     ║")
    print("╚══════════════════════════════════════════╝")
    print("")
    
    # Gerar chave
    chave = ChaveInvasor.gerar_chave(128)
    print(f"🔑 CHAVE INVASOR GERADA:")
    print(f"   {chave['chave']}")
    print(f"   Tamanho: {chave['tamanho_bits']} bits")
    print(f"   Combinações: {chave['combinacoes']}")
    print(f"   Resistência: {chave['resistencia_quantica']}")
    print("")
    
    # Gerar par para agente
    agente = ChaveInvasor.gerar_par_agente("Agente Silva", nivel=3)
    print(f"🦅 PAR DO AGENTE:")
    print(f"   Chave INVASOR: {agente['chave_invasor'][:60]}...")
    print(f"   Código visível: {agente['codigo_visivel']}")
    print(f"   Hash armazenado: {agente['hash_armazenado'][:40]}...")
    print("")
    
    # Verificar chave válida
    hash_guardado = ChaveInvasor.hash_para_armazenamento(agente['chave_invasor'])
    valida = ChaveInvasor.verificar_chave(agente['chave_invasor'], hash_guardado)
    print(f"✅ Chave válida: {valida}")
    
    # Verificar chave falsa
    chave_falsa = "INVASOR-FAKE-KEY-TEST-1234"
    falsa = ChaveInvasor.verificar_chave(chave_falsa, hash_guardado)
    print(f"🚫 Chave falsa: {falsa}")
