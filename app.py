from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Banco de dados atualizado com novos preços, promoções e Bot de Discord
PRODUTOS = [
    {
        "id": 1,
        "nome": "Landing Page",
        "descricao": "Uma página de conversão ultra-rápida de alta performance. Perfeita para vender produtos físicos, infoprodutos ou serviços digitais.",
        "preco_original": "R$ 120,00",
        "preco": "R$ 60,00",
        "porcentagem": "50% OFF",
        "destaque": False,
        "detalhes": [
            "Focada 100% em conversão e vendas",
            "Integração rápida com seu WhatsApp/Discord",
            "Configuração de Pixels (Meta/Google)",
            "Design moderno e otimizado para celulares",
            "Entrega rápida e suporte grátis"
        ]
    },
    {
        "id": 2,
        "nome": "Site Institucional",
        "descricao": "A estrutura de autoridade definitiva para sua empresa ou portfólio. Até 5 páginas interativas para mostrar autoridade no mercado.",
        "preco_original": "R$ 997,00",
        "preco": "R$ 450,00",
        "porcentagem": "55% OFF",
        "destaque": True,
        "detalhes": [
            "Até 5 páginas premium personalizadas",
            "Painel administrativo simples",
            "SEO otimizado para o Google",
            "Formulários de contato dinâmicos",
            "Suporte exclusivo por 30 dias"
        ]
    },
    {
        "id": 3,
        "nome": "Bot de Discord Personalizado",
        "descricao": "Sistemas completos de moderação automatizada, economia, registros, minigames e comandos exclusivos sob medida para sua comunidade.",
        "preco_original": "R$ 60,00",
        "preco": "R$ 30,00",
        "porcentagem": "50% OFF",
        "destaque": False,
        "detalhes": [
            "Comandos de barra inovadores (/)",
            "Moderação automática inteligente",
            "Integração de Banco de Dados",
            "Sistemas de cargos automáticos e VIPs",
            "Hospedagem 24/7 de alta estabilidade"
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', produtos=PRODUTOS)

@app.route('/produto/<int:produto_id>')
def produto(produto_id):
    produto = next((p for p in PRODUTOS if p['id'] == produto_id), None)
    if not produto:
        return "Serviço não encontrado", 404
    return render_template('produto.html', produto=produto)

@app.route('/checkout/<int:produto_id>', methods=['POST'])
def checkout(produto_id):
    nome_cliente = request.form.get('nome')
    whatsapp = request.form.get('whatsapp')
    
    produto = next((p for p in PRODUTOS if p['id'] == produto_id), None)
    if not produto:
        return "Serviço não encontrado", 404
        
    return render_template('sucesso.html', cliente=nome_cliente, produto=produto, whatsapp=whatsapp)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
