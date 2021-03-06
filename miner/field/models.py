from django.db import models


class Field(models.Model):
    CONSTANTS = {
        'FIELD_S': 's',
        'FIELD_M': 'm',
        'FIELD_L': 'l',
    }
    SIZES = {
        's': {
            'x': 10,
            'y': 10,
        },
        'm': {
            'x': 50,
            'y': 50,
        },
        'l': {
            'x': 100,
            'y': 100,
        },
    }
    CHOICE_SIZE = [
        ('s', 'Маленькое'),
        ('m', 'Среднее'),
        ('l', 'Большое'),
    ]
    size = models.CharField(
        max_length=2,
        choices=CHOICE_SIZE,
        default='s',
    )
    count_bomb = models.IntegerField()
