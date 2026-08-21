from flask import Flask, render_template

app = Flask(__name__)


PRODUTOS = [
    {
        "id": 1,
        "nome": "Landing Page",
        "descricao": "Página moderna e responsiva para divulgar seu negócio.",
        "preco": "R$ 149,90",
        "destaque": False
    },
    {
        "id": 2,
        "nome": "Site Profissional",
        "descricao": "Site completo para empresas, profissionais e pequenos negócios.",
        "preco": "R$ 299,90",
        "destaque": True
    },
    {
        "id": 3,
        "nome": "Site Premium",
        "descricao": "Site completo com design personalizado e recursos avançados.",
        "preco": "R$ 499,90",
        "destaque": False
    }
]


@app.route("/")
def index():
    return render_template("index.html", produtos=PRODUTOS)


@app.route("/produto/<int:produto_id>")
def produto(produto_id):
    produto_encontrado = next(
        (produto for produto in PRODUTOS if produto["id"] == produto_id),
        None
    )

    if produto_encontrado is None:
        return "Produto não encontrado", 404

    return render_template(
        "index.html",
        produtos=PRODUTOS,
        produto_selecionado=produto_encontrado
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)