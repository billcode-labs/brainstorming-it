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
        
    #def requirements(self):
    #    return Requirement.objects.filter(problem=self).order_by('-priority')

    
    def __unicode__(self):
        return self.name

class Requirement(models.Model):
    problem = models.ForeignKey(Problem)     #Many Requirements has One Problem
    name = models.CharField(max_length=32)
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
    problem = models.ForeignKey(Problem)      #Many Solutions has One Problem
    name = models.CharField(max_length=32)
    votes = models.IntegerField(default=0)
    description = models.TextField()
    
    class Meta:
        ordering = ['-votes']

    def __unicode__(self):
        return self.name

class Attachment(models.Model):
    solution = models.ForeignKey(Solution)    #Many Attachment has One Solution
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='uploads')

    def filename(self):
        return str(self.file)
        
    def __unicode__(self):
        return self.name

