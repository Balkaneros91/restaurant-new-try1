from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Table, Reservation, Booking
from .forms import ReservationForm

# Create your views here.


@login_required
def reserve_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.customer = request.user
            reservation.save()
            messages.success(request, 'Your reservation has been saved!')
            return redirect('book_a_table')
    else:
        form = ReservationForm()

    return render(request, 'reserve_table.html', {'form': form})


def view_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, customer=request.user)
    return render(request, 'view_reservation.html', {'reservation': reservation})


def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, customer=request.user)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Your reservation has been cancelled.')
        return redirect('book_a_table:home')
    return render(request, 'cancel_reservation.html', {'reservation': reservation})
