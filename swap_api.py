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
