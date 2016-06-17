from django.db import models


class ProfessorResponsavel(models.Model):
    matricula = models.CharField("Matricula",max_length=10)
    cpfProfessor=models.CharField("CPF",max_length=20)
    nome=models.CharField("Nome",max_length=100)
    def __str__(self):
        return self.nome

class MembroParticipante(models.Model):
    nome=models.CharField("Nome",max_length=100)
    email = models.EmailField("Email",max_length=100)
    telefone = models.CharField("Telefone",max_length=20)
    def __str__(self):
        return self.nome

class ProjetoPesquisa(models.Model):
    titulo=models.CharField("Titulo",max_length=200)
    dataInicio=models.DateField("Data de Inicio")
    dataTerminio = models.DateField("Data de Terminio")
    justificativa = models.CharField("Justificativa",max_length=200)
    metodologia = models.CharField("Metodologia",max_length=200)
    resultado=models.CharField("Resultado esperado",max_length=200)
    professorResponsavel=models.ForeignKey(ProfessorResponsavel,on_delete=models.PROTECT,verbose_name="Professor Responsavel")
    membro = models.ManyToManyField(MembroParticipante)
    def __str__(self):
        return self.titulo

class RegistroAcompanhamento(models.Model):
    estagioDesenvolvimento=models.CharField("Estagio desenvolvimento",max_length=200)
    dataRegistro = models.DateField("Data de Registro")
    DescricaoDesenvolvimento = models.CharField("Descrição",max_length=200)
    def __str__(self):
        return self.DescricaoDesenvolvimento

class Atividade(models.Model):
    descricao = models.CharField("Descrição",max_length=200)
    dataInicio = models.DateField("Data de Inicio")
    dataTerminio = models.DateField("Data de Terminio")
    custo = models.DecimalField("Custo",max_digits=10,decimal_places=2)
    projetoPesquisa= models.ForeignKey(ProjetoPesquisa,on_delete=models.PROTECT,verbose_name='Projeto Pesquisa')
    registro= models.ForeignKey(RegistroAcompanhamento,on_delete=models.PROTECT,verbose_name='Registro Acompanhamento')
    def __str__(self):
        return self.descricao
