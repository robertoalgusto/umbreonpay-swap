#!/usr/bin/env python3
from flask import Flask, request, jsonify
from flask_cors import CORS
from matching import engine
from custodia import CustodyContract
from multi_moeda import MultiMoeda
from ofuscacao_global import OfuscacaoGlobal

app = Flask(__name__)
CORS(app)
custody = CustodyContract()

@app.route("/api/swap/depositar", methods=["POST"])
def dep():
    d = request.json
    v = float(d.get("valor",0))
    mo = d.get("moeda","BRL")
    xmr = MultiMoeda.converter(v, mo, "XMR")
    f = engine.buscar_melhor(v)
    if not f: return jsonify({"erro":"Sem fornecedor"}),400
    c = custody.criar(d.get("cliente","anon"), f["id"], v, xmr)
    return jsonify({"ok":True,"contrato":c["id"],"xmr":xmr,"fornecedor":f["nome"],"pix":f.get("pix",""),"rota":OfuscacaoGlobal.rota(v)})

@app.route("/api/swap/saldo", methods=["POST"])
def saldo():
    d = request.json
    xmr = float(d.get("xmr",0))
    mo = d.get("moeda","BRL")
    vl = MultiMoeda.converter(xmr, "XMR", mo)
    return jsonify({"ok":True,"saldo":MultiMoeda.formatar(vl,mo)})

@app.route("/api/swap/moedas")
def moedas():
    return jsonify({"ok":True,"moedas":[{"cod":k,"sim":MultiMoeda.SIM.get(k,""),"cot":v} for k,v in MultiMoeda.COT.items()]})

@app.route("/")
def home():
    return jsonify({"app":"Umbreon Swap","status":"online"})

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)

# Novos endpoints de Link de Pagamento
from link_pagamento import LinkPagamento
lp = LinkPagamento()

@app.route("/api/link/criar", methods=["POST"])
def criar_link():
    d = request.json
    link = lp.criar(d.get("carteira",""), float(d.get("valor",0)), d.get("descricao",""))
    return jsonify({"ok":True,"link":link})

@app.route("/pagar/<codigo>")
def pagina_pagamento(codigo):
    link = lp.links.get(codigo)
    if not link: return "<h1>Link não encontrado</h1>", 404
    return f"""
    <html><head><meta charset='UTF-8'><title>Pagar com UBC</title>
    <style>body{{background:#0A0A0A;color:#FFF;font-family:sans-serif;text-align:center;padding:50px}}
    h1{{color:#C9A84C}} .valor{{font-size:48px;color:#C9A84C}} 
    button{{background:#C9A84C;color:#0A0A0A;border:none;padding:15px 40px;font-size:18px;cursor:pointer;border-radius:10px}}</style></head>
    <body><h1>UMBREON PAY</h1>
    <p>{link['descricao']}</p>
    <div class='valor'>{link['valor_ubc']} UBC</div>
    <p>Destino: {link['carteira_destino'][:20]}...</p>
    <button onclick="alert('Abra o app UmbreonPay para pagar')">PAGAR COM UBC</button>
    <p style='color:#888;margin-top:20px'>Válido até {link['valido_ate']}</p></body></html>
    """

@app.route("/api/link/pagar/<codigo>", methods=["POST"])
def pagar_link(codigo):
    d = request.json
    r = lp.pagar(codigo, d.get("carteira",""))
    return jsonify(r)

@app.route("/api/link/meus", methods=["POST"])
def meus_links():
    d = request.json
    return jsonify({"ok":True,"links":lp.listar_ativos(d.get("carteira",""))})
