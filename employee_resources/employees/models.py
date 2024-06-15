from django.db import models


class Position(models.Model):
    """Штатная должность."""
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.title


class Rank(models.Model):
    """Специальное звание/классный чин."""
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Звание'
        verbose_name_plural = 'Звания'

    def __str__(self):
        return self.title


class Employee(models.Model):
    """Сведения о сотруднике."""
    second_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, blank=True, null=True,
                             on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.second_name} {self.name} {self.patronymic}'
