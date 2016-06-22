from appprojetos.models import *

for e in ProjetoPesquisa.objects.all():
    print(e.titulo)
    print(end='membros do projetos')
    for i in e.membro.all():
        print(i.nome)
print("--------------------------- 4.a)")

for at in Atividade.objects.filter(dataInicio__month=5,
                                   dataInicio__year=2015):
    print(at)
print("---------------------------- 4.b)")

for me in MembroParticipante.objects.filter(nome__startswith='A'):
    print(me)

print("------------------------------ 4.c)")
ativ= ProjetoPesquisa.objects.all()
for e in ativ:
    total = 0
    print(e.titulo)
    for i in e.atividade_set.all():
        total+=i.custo
    print('Custo total ',total)

print("------------------------------- 4.d)")
#print(ProjetoPesquisa.objects.all())

#{1:s}