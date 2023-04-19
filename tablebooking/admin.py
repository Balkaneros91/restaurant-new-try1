from django.contrib import admin
# from django.utils.html import format_html
from .models import Booking
# from .models import Table, Customer


# class TableAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'is_available')
#     list_filter = ('is_available',)
#     actions = ['make_available', 'make_unavailable']

#     def make_available(self, request, queryset):
#         queryset.update(is_available=True)
#         self.message_user(request, 'Selected tables are now available.')
#     make_available.short_description = 'Make selected tables available'

#     def make_unavailable(self, request, queryset):
#         queryset.update(is_available=False)
#         self.message_user(request, 'Selected tables are now unavailable.')
#     make_unavailable.short_description = 'Make selected tables unavailable'


# class BookingAdmin(admin.ModelAdmin):
#     list_display = ('id', 'customer', 'table', 'date', 'time', 'party_size')
#     list_filter = ('table', 'date',)
#     search_fields = ('customer__first_name', 'customer__last_name', 'customer__email', 'table__name')

#     def customer(self, obj):
#         return obj.customer.full_name
#     customer.admin_order_field = 'customer__last_name'

#     def table(self, obj):
#         return format_html("<a href='/admin/restaurant/table/{}/change/'>{}</a>", obj.table.id, obj.table.name)
#     table.admin_order_field = 'table__name'


# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'full_name', 'email')
#     search_fields = ('first_name', 'last_name', 'email')

#     def full_name(self, obj):
#         return f"{obj.first_name} {obj.last_name}"
#     full_name.admin_order_field = 'last_name'


# admin.site.register(Table, TableAdmin)
# admin.site.register(Booking, BookingAdmin)
# admin.site.register(Customer, CustomerAdmin)

admin.site.register(Booking)
