
def listar_aluno_by_id_service(id, alunos):
    for aluno in alunos:
        if (aluno["id"] == id):
            return aluno
    
    return None

def verificacao_campos_aluno(aluno):
    if "nome" not in aluno:
        return ("Campo 'nome' é obrigatório")
    if "matricula" not in aluno:
        return ("Campo 'matricula' é obrigatório")
    if "curso" not in aluno:
        return ("Campo 'curso' é obrigatório")
    if "media" not in aluno:
        return ("Campo 'media' é obrigatório")
    
    return None

def atualizar_aluno_by_id_service(id, atualizacao_aluno, alunos):
    for aluno in alunos:
        if (aluno["id"] == id):
            atualizacao_aluno.pop("id", None)
            aluno.update(atualizacao_aluno)
            return aluno
        
    return None

def deletar_aluno_by_id_service(id, alunos):
    for aluno in alunos:
        if (aluno["id"] == id):
            alunos.remove(aluno)
            return True
    return None