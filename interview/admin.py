from django.contrib import admin
from interview.models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
                 ('Question',               {'fields': ['question_text']}),
                 ('Answer', {'fields': ['answer_text']}),
                 ]

admin.site.register(Question)





# Register your models here.

