from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=32)

    class Meta():
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=32)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    #parent_project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name