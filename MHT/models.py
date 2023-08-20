from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class ToDoItem(models.Model):
    pass

class participant(models.Model):
    id = models.AutoField(primary_key=True)
    
    email = models.EmailField(
        db_column="my_email",  # allows to avoid migrating to a different column
    )

    phone = models.CharField(
        max_length=17,
        db_column="my_phone",  # allows to avoid migrating to a different column
    )

    FIO = models.CharField(
        db_column="my_FIO",max_length = 150,blank = True  # allows to avoid migrating to a different column
    )

    @classmethod
    def create(cls,FIO,phone,email):
        participant = cls(phone=phone,email=email,FIO = FIO)

    def __str__(self):
        return self.FIO

class teamMentor(models.Model):
    id = models.AutoField(primary_key=True)
    FIO = models.CharField(
        db_column="mentor_FIO",
        max_length = 200
    )
    @classmethod
    def create(cls,FIO):
        teamMentor = cls(FIO = FIO)

    def __str__(self):
        return self.FIO

class team(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(
        max_length=200,
        db_column="team_name"
    )

    region  = models.CharField(
        max_length=200,
        db_column='team_region',
        blank=True
    )

    members = models.ManyToManyField(
        "participant",
        through='membership'
    )

    mentor = models.ManyToManyField(
        'teamMentor'
    )

    @classmethod
    def create(cls, name):
        team = cls(name = name)

    def __str__(self):
        return self.name

class membership(models.Model):
    class Meta():
        db_table = 'membership'

    id = models.AutoField(primary_key=True)

    participant = models.ForeignKey(
        participant,
        on_delete=models.CASCADE
    )

    team = models.ForeignKey(
        team,
        on_delete=models.CASCADE
    )

    school = models.TextField(default='')

    participant_class = models.IntegerField("participant_class")

    year = models.IntegerField()

    letter = models.TextField(blank=True)
class FullTable(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name = "ФИО"
    )
    email = models.EmailField(verbose_name= "Почта")

    phone = models.CharField(
        max_length=200,
        verbose_name="Телефон"
    )

    team = models.CharField(
        max_length=200,
    )