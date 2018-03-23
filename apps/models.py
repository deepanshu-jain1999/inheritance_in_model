from django.db import models


class Student(models.Model):
    """
    Abstract based inheritance
    here this model alone have no signifance
    but with other model it will include these field into that model
    so here name will include in Account class
    """

    """
    here related_name will we 'apps_account_related' 
    and rel_query name = apps_account
    """
    name = models.CharField(max_length=100,
                            primary_key=True,
                            # related_name="%(app_label)s_%(class)s_related",
                            # related_query_name="%(app_label)s_%(class)s",
                           )

    class Meta:
        abstract = True


class Account(Student):
    gmail = models.CharField(max_length=300)
    github = models.CharField(max_length=300)


# move to multiple inheritance


class Place(models.Model):
    """
    In multiple inheritance
    1. Place have only own field while Restaurant have both class field
    2. If we create a restaurant model then place already will made but reverse not true
    3.

    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

# Proxy model


class Person(models.Model):
    """
    They use the original models as an instance ans shared one table in database
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class MyPerson(Person):
    class Meta:
        proxy = True
