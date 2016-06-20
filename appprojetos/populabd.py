from django.db import transaction,IntegrityError
from appprojetos.models import *

# Criando professor resp

profess1 =ProfessorResponsavel(matricula='1022',cpfProfessor='000.111.222-33',nome='jorge',)
profess2 =ProfessorResponsavel(matricula='2002',cpfProfessor='000.110.222-33',nome='Bruno')
profess3 =ProfessorResponsavel(matricula='3032',cpfProfessor='000.101.222-33',nome='Fernando')

profess1.save()
profess2.save()
profess3.save()

projeto1 = ProjetoPesquisa(titulo='sofware livre para todos',dataInicio='2016-02-27',dataTerminio='2016-12-27',professorResponsavel=profess2)
projeto2 = ProjetoPesquisa(titulo='Programação para crianças',dataInicio='2015-03-27',dataTerminio='2016-07-07',professorResponsavel=profess3)
projeto3 = ProjetoPesquisa(titulo='Estudo sobre jovens',dataInicio='2016-01-02',dataTerminio='2016-11-19',professorResponsavel=profess1)

projeto1.save()
projeto2.save()
projeto3.save()

registro1= RegistroAcompanhamento(estagioDesenvolvimento='nivel 2',dataRegistro='2015-04-04',DescricaoDesenvolvimento='A atividade está indo mais ou menos')
registro2= RegistroAcompanhamento(estagioDesenvolvimento='nivel 2',dataRegistro='2016-01-23',DescricaoDesenvolvimento='A atividade está indo bem')
registro3= RegistroAcompanhamento(estagioDesenvolvimento='nivel 2',dataRegistro='2016-03-03',DescricaoDesenvolvimento='A atividade está indo mal')
registro4= RegistroAcompanhamento(estagioDesenvolvimento='nivel 2',dataRegistro='2016-01-23',DescricaoDesenvolvimento='A atividade está indo dificil')
registro5= RegistroAcompanhamento(estagioDesenvolvimento='nivel 2',dataRegistro='2016-04-03',DescricaoDesenvolvimento='A atividade está indo bem')

registro1.save()
registro2.save()
registro3.save()
registro4.save()
registro5.save()

atividade1=Atividade(descricao='estudar como ensinar crianças',dataInicio='2015-05-03',dataTerminio='2016-01-01',projetoPesquisa=projeto2,custo=2000,
                     registro=registro1)
atividade2=Atividade(descricao='estudar a joventude',dataInicio='2016-01-23',dataTerminio='2016-03-01',projetoPesquisa=projeto3,custo=3000,
                     registro=registro2)
atividade3=Atividade(descricao='estudar sobre software',dataInicio='2016-03-03',dataTerminio='2016-06-01',projetoPesquisa=projeto1,custo=4000,
                     registro=registro3)
atividade4=Atividade(descricao='Levantamento de dados sobre modernidade',dataInicio='2016-01-23',dataTerminio='2016-05-01',projetoPesquisa=projeto3,
                     custo=2500,registro=registro4)
atividade5=Atividade(descricao='como disponibilizar dados ao publico',dataInicio='2016-04-03',dataTerminio='2016-12-01',projetoPesquisa=projeto1,
                     custo=3300,registro=registro5)

atividade1.save()
atividade2.save()
atividade3.save()
atividade4.save()
atividade5.save()

membro1 = MembroParticipante(nome='jose',email='js@gmail.com',telefone='0000-9922')
membro2 = MembroParticipante(nome='Maria',email='mar@gmail.com',telefone='9100-9922')
membro3 = MembroParticipante(nome='Marcelo',email='marc@gmail.com',telefone='8000-9922')
membro4 = MembroParticipante(nome='Claudio',email='cla@gmail.com',telefone='9830-9922')
membro5 = MembroParticipante(nome='Amanda',email='lai@gmail.com',telefone='9800-9922')
membro6 = MembroParticipante(nome='Karol',email='karol@gmail.com',telefone='8800-9922')
membro7 = MembroParticipante(nome='Ana',email='ana@gmail.com',telefone='9200-9922')
#bj

membro1.save()
membro2.save()
membro3.save()
membro4.save()
membro5.save()
membro6.save()
membro7.save()

projeto1.membro.add(membro1,membro4)
projeto2.membro.add(membro2,membro3)
projeto3.membro.add(membro5,membro1)

