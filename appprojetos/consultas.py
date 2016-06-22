from appprojetos.models import *

for e in ProjetoPesquisa.objects.all():
    print(e.titulo)
    print(end='membros do projetos\n')
    for i in e.membro.all():
        print(i.nome)
print("--------------------------- 4.a)")


print("------------------------------ 4.c)")
ativ= ProjetoPesquisa.objects.all()
for e in ativ:
    soma = 0
    print(e.titulo)
    for i in e.atividade_set.all():
        soma+=i.custo
    print('Custo total ',soma)

print("------------------------------- 4.d)")
#print(ProjetoPesquisa.objects.all())

#{1:s}