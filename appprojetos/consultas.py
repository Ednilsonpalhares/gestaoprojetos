from appprojetos.models import *

for projeto in ProjetoPesquisa.objects.all():
    print("Projeto: {0:s} - Membros: {1:s}".format(ProjetoPesquisa.titulo, ProjetoPesquisa.membro))

atividade=Atividade.objects.filter(dataInicio__month=5, dataInicio__year=2015)
print(atividade)

pessoas=MembroParticipante.objects.filter(nome__startswith='A')
print(pessoas)

