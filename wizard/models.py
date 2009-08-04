from django.db import models
from pardusman.wizard.fields import DictionaryField


# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	activation_key = models.CharField(max_length=40)
	key_expires = models.DateTimeField()

class Dependency(models.Model):
	name = models.CharField(max_length=60,primary_key=True)
	
class Package(models.Model):
	name = models.CharField(max_length=60,primary_key=True)
	size = models.IntegerField(max_length=60)
	part_of = models.CharField(max_length=60)
	dependencies = models.ManyToManyField(Dependency)

class Components(models.Model):
	name = models.CharField(max_length=60,primary_key=True)
	packages = models.ManyToManyField(Dependency)

class Repository(models.Model):
	name = models.CharField(max_length=60,primary_key=True)
	size = models.IntegerField(max_length=60)
	inst_size = models.IntegerField(max_length=60)
	packages = models.ManyToManyField(Package)
	components = models.ManyToManyField(Components)

class scheduled_distro(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    log_url = models.URLField()
    image_title = models.CharField(max_length=60)
    image_url = models.URLField()
    image_type = models.CharField(max_length=60)
    project_url = models.URLField()
    progress = models.CharField(max_length=60)

class Userlogs(models.Model):
    username = models.CharField(max_length=60,primary_key=True)
    scheduled_tasks = models.ManyToManyField(scheduled_distro)

class buildfarm_queue(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    project_file = models.URLField()

class onprogress_queue(models.Model):
    id = models.IntegerField(primary_key=True)
    work_dir = models.URLField()
    image_file = models.URLField()
    status = models.CharField(max_length=60)

