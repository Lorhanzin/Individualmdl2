  while True:
        x = input(f'Nota na etapa de {y}: ')
        if x.isdigit():
            break
        else:
            print('Dígito inválido. Favor tente novamente!')
    return int(x)

def procurar(notas, estudantes):
    aprovados = []
    for nome, notas_candidato in estudantes.items():
        if all(notas_candidato[i] >= notas[i % 4] for i in range(4)):
            aprovados.append(nome)
    if aprovados:
        print(f'Alunos aprovados: {aprovados}')
    else:
        print('Nenhum aluno encontrado.')

alunos = {}
while True:
    nome = input('Digite o nome do candidato: ')
    notas_candidato = [verifica(y) for y in ['entrevista', 'teste teórico', 'teste prático', 'soft skills']]
    alunos[nome] = notas_candidato
    novo_usuário = input('Deseja cadastrar novo aluno? (sim/não)')
    if novo_usuário != 'sim':
        break

notas = [int(input(f'Nota mínima para a etapa de {y}: ')) for y in ['entrevista', 'teste teórico', 'teste prático', 'soft skills']]

df = pd.DataFrame(alunos, index=['entrevista', 'teste teórico', 'teste prático', 'soft skills'])
print('Candidatos que realizaram as provas:')
print(df.T)

procurar(notas, alunos)
