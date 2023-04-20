from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingTableForm


def book_a_table(request):
    booking_form = BookingTableForm()

    if request.method == 'POST':
        booking_form = BookingTableForm(request.POST)

        if booking_form.is_valid():
            booking_form.save()
            messages.success(request, 'Your booking has been confirmed.')
            return redirect('booking_confirmation')

    context = {'form': booking_form}

    return render(request, 'tablebooking/booking.html', context)


def booking_confirmation(request):
    latest_booking = Booking.objects.last()
    context = {'booking': latest_booking}
    return render(request, 'tablebooking/booking_confirmation.html', context)


def edit_booking(request, booking_id):
    # Retrieve the booking object to edit
    booking = get_object_or_404(Booking, id=int(booking_id))

    if request.method == 'POST':
        form = BookingTableForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been updated.')
            return redirect('booking_confirmation')
    else:
        form = BookingTableForm(instance=booking)

    context = {'form': form}
    return render(request, 'tablebooking/edit_booking.html', context)


def delete_booking(request, booking_id):
    # Retrieve the booking object to delete
    booking = get_object_or_404(Booking, id=int(booking_id))

    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Your booking has been deleted.')
        return redirect('booking_list')

    context = {'booking': booking}
    return render(request, 'tablebooking/delete_booking.html', context)
