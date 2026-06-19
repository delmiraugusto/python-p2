from flask import Flask, request

from utils import deletar_aluno_by_id_service, verificacao_campos_aluno, listar_aluno_by_id_service, atualizar_aluno_by_id_service

app = Flask(__name__)

alunos = [
    {
        "id": 1, 
        "nome": "Delmir Augusto", 
        "matricula": "12410865",
        "curso": "Engenharia da Computação",
        "media": 8.5,
    }
]

id_auto_increment: int = 1

@app.route("/")
def inicio():
    return "Minha API Flask"

@app.route("/alunos")
def listar_alunos():
    return {"alunos": alunos}

@app.route("/alunos/<int:id>")
def listar_aluno_by_id(id):

    aluno = listar_aluno_by_id_service(id, alunos)
    if (aluno is None):
        return {"message" : "Aluno não encontrado"}, 404
    
    return {"Aluno" : aluno}


@app.route("/alunos", methods=["POST"])
def cadastrar_aluno():

    global id_auto_increment

    aluno = request.json
   
    if verificacao_campos_aluno(aluno):
        return {"message": verificacao_campos_aluno(aluno)}, 400
    
    id_auto_increment += 1
    aluno["id"] = id_auto_increment

    alunos.append(aluno)
    
    return {
            "message": "Aluno cadastrado com sucesso",
            "Aluno": aluno
        }, 201

@app.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno_by_id(id):
    aluno = request.json

    dados = atualizar_aluno_by_id_service(id, aluno, alunos)
    if dados is None:
        return {"message" : "Aluno não encontrado"}, 404

    return {
        "message": "Aluno atualizado com sucesso",
        "aluno": dados
    }

@app.route("/alunos/<int:id>", methods=["DELETE"])
def deletar_aluno_by_id(id):
    aluno_deletedo = deletar_aluno_by_id_service(id, alunos)

    if aluno_deletedo is None:
        return {"message" : "Aluno não encontrado"}, 404
    
    return {"message" : "Aluno deletado com sucesso"}, 200

 
if __name__ == "__main__":
    app.run(debug=True)