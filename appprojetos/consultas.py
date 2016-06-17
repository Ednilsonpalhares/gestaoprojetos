from appprojetos.models import *

for p in ProfessorResponsavel.objects.all():
    print("Descrição: {0:s} -Sigla: {1:s}".format(p.nome, p.matricula))

