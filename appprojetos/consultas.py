from appprojetos.models import *

for projeto in ProjetoPesquisa.objects.all():
    print(projeto.titulo)
    print(end='Membros do projetos\n')
    for mem in projeto.membro.all():
        print(mem.nome)
print("--------------------------- 4.a)")

for atividade in Atividade.objects.filter(dataInicio__month=5,dataInicio__year=2015):
    print(atividade)
print("---------------------------- 4.b)")

for memproparticipante in MembroParticipante.objects.filter(nome__startswith='A'):
    print(memproparticipante)

print("------------------------------ 4.c)")
projetoPesqui= ProjetoPesquisa.objects.all()
for ativida in projetoPesqui:
    total = 0
    for i in ativida.atividade_set.all():
        total+=i.custo
    print('Custo total do projeto %s: R$ %.2f'%(ativida.titulo,total))

print("------------------------------- 4.d)")
#print(ProjetoPesquisa.objects.all())

#{1:s}