#!/usr/bin/env python3
"""
╔══════════════════════════════════════════╗
║   VÍDEO INSTITUCIONAL — ROTEIRO          ║
║   Animação de lançamento                 ║
╚══════════════════════════════════════════╝
"""

class VideoInstitucional:
    ROTEIRO = {
        "duracao": "60 segundos",
        "estilo": "Animação 3D escura com detalhes dourados",
        "musica": "Orquestral épico com batidas eletrônicas graves",
        "cenas": [
            {"tempo": "0-5s", "cena": "Tela preta. Som de águia. Brasão da UmbreonPay surge com brilho dourado."},
            {"tempo": "5-15s", "cena": "Dados digitais fluindo. Texto: 'SEU DINHEIRO NÃO É SEGURO'. Dados sendo interceptados por olhos."},
            {"tempo": "15-25s", "cena": "Escudo TWS aparece bloqueando os olhos. 4 camadas de proteção se sobrepõem."},
            {"tempo": "25-35s", "cena": "Texto: 'CRIPTOGRAFIA INQUEBRÁVEL'. OTP + Abecedário + Fragmentação + AES-256."},
            {"tempo": "35-45s", "cena": "Globo terrestre com pontos dourados. Texto: '100+ PAÍSES'. Conexões P2P."},
            {"tempo": "45-55s", "cena": "Celular com pagamento NFC. Texto: 'PAGUE POR APROXIMAÇÃO'. Maquininha aprovando."},
            {"tempo": "55-60s", "cena": "Brasão final. Texto: 'UMBREONPAY — POTESTAS IN UMBRA'. Link do site."},
        ],
        "call_to_action": "Abra sua conta agora: link na descrição",
        "hashtags": ["#UmbreonPay", "#PotestasInUmbra", "#Criptomoedas", "#Privacidade", "#Monero"]
    }
    
    @classmethod
    def exportar_roteiro(cls):
        roteiro = f"""
╔══════════════════════════════════════════╗
║   ROTEIRO — VÍDEO INSTITUCIONAL          ║
╠══════════════════════════════════════════╣
║   Duração: {cls.ROTEIRO['duracao']}                    ║
║   Estilo: {cls.ROTEIRO['estilo']}  ║
║   Música: {cls.ROTEIRO['musica']} ║
╚══════════════════════════════════════════╝

"""
        for c in cls.ROTEIRO['cenas']:
            roteiro += f"[{c['tempo']}] {c['cena']}\n\n"
        
        roteiro += f"\n📢 Call to Action: {cls.ROTEIRO['call_to_action']}\n"
        roteiro += f"🏷️ Hashtags: {' '.join(cls.ROTEIRO['hashtags'])}\n"
        return roteiro

print("✅ Roteiro do Vídeo pronto")
