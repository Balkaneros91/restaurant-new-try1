from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from .forms import BookingTableForm


@login_required
def book_a_table(request):
    booking_form = BookingTableForm()

    if request.method == 'POST':
        booking_form = BookingTableForm(request.POST)
        print(request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking has been confirmed.')
            return redirect('booking_confirmation')

    context = {'form': booking_form}

    return render(request, 'table_booking/table_booking_form.html', context)


def booking_confirmation(request):
    latest_booking = Booking.objects.last()
    context = {'booking': latest_booking}
    return render(request, 'table_booking/booking_confirmation.html', context)
