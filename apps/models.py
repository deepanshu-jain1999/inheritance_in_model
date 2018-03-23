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
                            related_name="%(app_label)s_%(class)s_related",
                            related_query_name="%(app_label)s_%(class)s",)

    class Meta:
        abstract = True


class Account(Student):
    gmail = models.CharField(max_length=300)
    github = models.CharField(max_length=300)

