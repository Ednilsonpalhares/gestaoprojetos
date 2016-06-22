from appprojetos.models import *

for projeto in ProjetoPesquisa.objects.all():
    print(projeto.titulo,end=' membros do projeto \n')
    for membro in projeto.membro.all():
        print(membro.nome)

for atividade in Atividade.objects.filter(dataInicio__month=5, dataInicio__year=2015):
    print(atividade)

for pessoas in MembroParticipante.objects.filter(nome__startswith='A'):
    print(pessoas)
