# coding: utf-8
        
from django.contrib import admin
from django.db.models import TextField
from django.forms import Textarea

from .models import Project, Requirement, Problem, Solution, Attachment

#class RequirementInline(admin.TabularInline):
#    model = Requirement
    
#class SolutionInline(admin.TabularInline):
#    model = Solution
    
class ProblemAdmin(admin.ModelAdmin):
    #inlines = [
    #    RequirementInline,
    #    SolutionInline,
    #]
    list_display = ('name', 'vote')
    list_filter = ('project',)


class AttachmentInline(admin.TabularInline):
    model = Attachment

class SolutionAdmin(admin.ModelAdmin):
    inlines = [
        AttachmentInline,
    ]
    list_display = ('name', 'like', 'unlike')
    list_filter = ('problem',)


    

admin.site.register(Project)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Solution, SolutionAdmin)
