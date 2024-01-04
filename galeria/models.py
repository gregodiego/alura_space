from django.db import models


class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta'),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100, blank=False, null=False, choices=OPCOES_CATEGORIA, default='')
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return f'fotografia [nome={self.nome}]'
