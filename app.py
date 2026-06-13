from flask import Flask, jsonify, request
from faker import Faker
from datetime import datetime
import random

app = Flask(__name__)
fake = Faker('pt_BR')

alunos = []
proximo_id_aluno = 1

CURSOS = [
    "Ciência da Computação",
    "Sistemas de Informação",
    "Análise e Desenvolvimento de Sistemas",
    "Engenharia da Computação",
    "Administração",
    "Direito",
    "Engenharia Civil",
    "Medicina",
    "Psicologia",
    "Arquitetura",
]


def gerar_alunos(qtd=20):
    """Gera alunos fictícios usando Faker"""
    global proximo_id_aluno
    for _ in range(qtd):
        aluno = {
            "id": proximo_id_aluno,
            "nome": fake.name(),
            "email": fake.email(),
            "matricula": f"{datetime.now().year}{random.randint(1000, 9999)}",
            "curso": random.choice(CURSOS),
            "data_nascimento": fake.date_of_birth(
                minimum_age=17, maximum_age=60
            ).isoformat(),
            "telefone": fake.phone_number(),
            "ativo": random.choice([True, True, True, False]),
        }
        alunos.append(aluno)
        proximo_id_aluno += 1


gerar_alunos()


@app.route('/alunos', methods=['GET'])
def listar_alunos():
    return jsonify({"alunos": alunos, "total": len(alunos)})


@app.route('/alunos/<int:id>', methods=['GET'])
def obter_aluno(id):
    aluno = next((a for a in alunos if a["id"] == id), None)
    if not aluno:
        return jsonify({"erro": "Aluno nao encontrado"}), 404
    return jsonify(aluno)


@app.route('/alunos', methods=['POST'])
def criar_aluno():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Corpo da requisicao vazio"}), 400
    if not dados.get("nome") or not dados.get("curso"):
        return jsonify({"erro": "Campos obrigatorios: nome, curso"}), 400

    global proximo_id_aluno
    aluno = {
        "id": proximo_id_aluno,
        "nome": dados["nome"],
        "email": dados.get("email", ""),
        "matricula": f"{datetime.now().year}{random.randint(1000, 9999)}",
        "curso": dados["curso"],
        "data_nascimento": dados.get("data_nascimento", ""),
        "telefone": dados.get("telefone", ""),
        "ativo": dados.get("ativo", True),
    }
    alunos.append(aluno)
    proximo_id_aluno += 1
    return jsonify(aluno), 201


@app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    aluno = next((a for a in alunos if a["id"] == id), None)
    if not aluno:
        return jsonify({"erro": "Aluno nao encontrado"}), 404

    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Corpo da requisicao vazio"}), 400

    aluno["nome"] = dados.get("nome", aluno["nome"])
    aluno["email"] = dados.get("email", aluno["email"])
    aluno["curso"] = dados.get("curso", aluno["curso"])
    aluno["data_nascimento"] = dados.get("data_nascimento", aluno["data_nascimento"])
    aluno["telefone"] = dados.get("telefone", aluno["telefone"])
    aluno["ativo"] = dados.get("ativo", aluno["ativo"])

    return jsonify(aluno)


@app.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    aluno = next((a for a in alunos if a["id"] == id), None)
    if not aluno:
        return jsonify({"erro": "Aluno nao encontrado"}), 404

    alunos.remove(aluno)
    return jsonify({"mensagem": "Aluno removido com sucesso"})


if __name__ == '__main__':
    print(f"Servidor rodando em http://localhost:5000")
    print(f"Total de alunos carregados: {len(alunos)}")
    app.run(debug=True)
