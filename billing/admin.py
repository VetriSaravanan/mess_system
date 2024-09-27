from django.contrib import admin
from .models import Bill

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('student', 'total_amount', 'discount', 'final_amount', 'date_generated')
    list_filter = ('date_generated',)
    search_fields = ('student__name',)

    def final_amount(self, obj):
        return obj.calculate_total()  # Calculate final amount using model method
    final_amount.short_description = 'Final Amount'  # Set a custom name for the column
