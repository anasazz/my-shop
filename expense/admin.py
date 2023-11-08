from django.contrib import admin

from .models import Expense, ExpenseTransaction


# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    pass




class ExpenseTransactionAdmin(admin.ModelAdmin):
    list_display = ['number', 'date', 'notes', 'expense', 'value']
    fields = ['number', 'date', 'expense', 'value', 'notes']
    list_filter = ['expense']
    date_hierarchy = 'date'
    search_fields = ['number', 'notes']

admin.site.register(ExpenseTransaction, ExpenseTransactionAdmin)
admin.site.register(Expense)

