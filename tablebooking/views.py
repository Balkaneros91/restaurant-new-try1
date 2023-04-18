from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags
from datetime import timedelta

from .models import Table, Reservation, Booking
from .forms import BookingForm


def index(request):
    tables = Table.objects.all()
    context = {
        'tables': tables,
        'opening_times': [table.opening_time for table in tables],
        'closing_times': [table.closing_time for table in tables],
    }
    return render(request, 'index.html', context)


# @login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            table = booking.table

            # Check if reservation time is within opening and closing times
            now = timezone.now()
            if not (table.opening_time <= booking.reservation_time <= table.closing_time):
                messages.error(request, f"Reservation time should be between {table.opening_time.strftime('%H:%M')} and {table.closing_time.strftime('%H:%M')}.")
                return render(request, 'booking_form.html', {'form': form})

            # Check if reservation time is at least 2 hours after the current time
            if booking.reservation_time < now + timedelta(hours=2):
                messages.error(request, "Reservation time should be at least 2 hours from now.")
                return render(request, 'booking_form.html', {'form': form})

            # Check if reservation time is at least 2 hours before closing time
            if booking.reservation_time > table.closing_time - timedelta(hours=2):
                messages.error(request, f"Reservation time should be at least 2 hours before the closing time ({table.closing_time.strftime('%H:%M')}).")
                return render(request, 'booking_form.html', {'form': form})

            # Check if there is already a booking for the same table at the same time
            if Booking.objects.filter(table=table, reservation_time=booking.reservation_time).exists():
                messages.error(request, "This table is already booked at the selected time.")
                return render(request, 'booking_form.html', {'form': form})

            # if request.user.is_authenticated:
            #     booking.customer_name = request.user.username
            #     email = request.user.email
            # else:
            #     booking.customer_name = 'Anonymous'
            #     email = form.cleaned_data['email']

            booking.customer_name = request.user.username
            booking.save()
            messages.success(request, 'Booking created successfully.')

            email = request.user.email if request.user.is_authenticated else form.cleaned_data['email']
            # send_confirmation_email(email, 'created', booking)
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})


@login_required
def booking_list(request):
    if request.user.is_superuser:
        bookings = Booking.objects.all()
    else:
        bookings = Booking.objects.filter(customer_name=request.user.username)
    return render(request, 'booking_list.html', {'bookings': bookings})


@login_required
def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save()
            messages.success(request, 'Booking updated successfully.')
            send_confirmation_email(request.user.email, 'updated', booking)
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking_form.html', {'form': form, 'booking': booking})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking deleted successfully.')
        send_confirmation_email(request.user.email, 'deleted', booking)
        return redirect('booking_list')
    return render(request, 'booking_confirm_delete.html', {'booking': booking})


def send_confirmation_email(email, action, booking):
    subject = f'Booking {action} confirmation'
    html_message = render_to_string('booking_confirmation_email.html', {'booking': booking})
    plain_message = strip_tags(html_message)
    from_email = 'noreply@example.com'
    send_mail(subject, plain_message, from_email, [email], html_message=html_message)
