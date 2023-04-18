from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Reservation, Booking, Table

# Register your models here.


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'table_name', 'table_capacity', 'date', 'time')
    list_filter = ('date', 'time', 'table__name')
    search_fields = ('customer__username', 'table__name')
    date_hierarchy = 'date'
    ordering = ('date', 'time')

    def get_queryset(self, request):
        # Override default queryset to only include reservations for the current user
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(customer=request.user)

    def table_name(self, obj):
        return obj.table.name

    def table_capacity(self, obj):
        return obj.table.capacity

    def save_model(self, request, obj, form, change):
        # Override default save method to automatically set the customer field to the current user
        if not obj.customer:
            obj.customer = request.user
        obj.save()


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'table', 'date', 'time')
    list_filter = ('date', 'time')
    search_fields = ('customer_name', 'table__name')
    date_hierarchy = 'date'
    ordering = ('date', 'time')


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')


class ReservationInline(admin.TabularInline):
    model = Reservation
    extra = 0
    readonly_fields = ('table', 'date', 'time')


class CustomUserAdmin(UserAdmin):
    inlines = [ReservationInline]
