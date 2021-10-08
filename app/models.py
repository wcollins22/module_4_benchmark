from django.db import models
from django.shortcuts import get_object_or_404

# Create your models here.
class Job(models.Model):
    role_name = models.CharField(max_length=50)
    role_description = models.CharField(max_length=100)
    company_name = models.CharField(max_length=50)
    role_requirements = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    minimum_salary = models.IntegerField()
    maximum_salary = models.IntegerField()


def create_job(role_name, role_description, company_name, role_requirements, location, minimum_salary, maximum_salary):
    job = Job(role_name=role_name, role_description=role_description, company_name=company_name, role_requirements=role_requirements, location=location, minimum_salary=minimum_salary, maximum_salary=maximum_salary)
    job.save()
    return job

def view_all():
    return Job.objects.all()

def view_location(location):
    return Job.objects.get(location=location)

def view_role(role_name):
    return Job.objects.get(role_name=role_name)

def good_sal(goal):
    for j in Job.objects.all():
        if j.minimum_salary <= goal <= j.maximum_salary:
            return j
            


def update_location(id, new_location):
    job = get_object_or_404(Job, id=id)
    job.location = new_location
    job.save()

def delete_job(id):
    job = get_object_or_404(Job, id=id)
    job.delete()



