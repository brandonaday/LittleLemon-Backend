from django.contrib import admin
from .models import Menu,Booking

# Register your models here.
#my_models = [Menu,Booking] # iterable list for multiple models

#admin.site.register(my_models)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'No_of_guests', 'BookingDate')
    list_filter = ('BookingDate',)
    search_fields = ('name',)
    date_hierarchy = 'BookingDate'
    list_per_page = 20  # Show 20 records per page

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Price', 'Inventory')
    list_filter = ('Inventory',)
    search_fields = ('Title',)
    list_per_page = 20  # Show 20 records per page
    list_editable = ('Price', 'Inventory')

    fieldsets = (
        (None, {
            'fields': ('Title', 'Price', 'Inventory')
        }),
        ('Additional Information', {
            'fields': (),  
            'classes': ('collapse',)
        }),
    )