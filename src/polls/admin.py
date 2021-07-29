from django.contrib import admin

from . models import Question, Choice

# Register your models here.

# Associated models
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    # Add field groups in Admin
    fieldsets = [
        ('Question', {
            'fields': ['question_text']
        }),
        ('Date Information', {
            'fields': ['pub_date']
        })
    ]
    inlines = [ChoiceInLine]

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']

    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)