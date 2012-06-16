from django.db import models

# models
class Project(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class Problem(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=32)
    priority = models.IntegerField(default=1)

    class Meta:
        ordering = ['priority']
    
    def __unicode__(self):
        return self.name

class Requirement(models.Model):
    name = models.CharField(max_length=32)
    problem = models.ForeignKey(Problem)
    priority = models.IntegerField(default=1)
    user = models.CharField(u'As a', max_length=32, blank=True)
    action = models.TextField(u'I want to', blank=True)
    detail = models.TextField(u'So that', blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['priority']

    def __unicode__(self):
        return self.name


class Solution(models.Model):
    name = models.CharField(max_length=32)
    problem = models.ForeignKey(Problem)
    votes = models.IntegerField(default=0)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Attachment(models.Model):
    name = models.CharField(max_length=32)
    solution = models.ForeignKey(Solution)
    attachment = models.FileField(upload_to='uploads')

    def __unicode__(self):
        return self.name

