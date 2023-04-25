from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from table_booking.models import Booking
from table_booking.forms import BookingTableForm

# Create your views here.


@login_required
def booking_list(request):
    # bookings = Booking.objects.filter(user=request.user)
    bookings = Booking.objects.filter(user_id=request.user.id)

    context = {'bookings': bookings}
    return render(request, 'users_bookings/booking_list.html', context)


@login_required
def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user_id=request.user.id)
    if request.method == 'POST':
        form = BookingTableForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingTableForm(instance=booking)
    context = {'form': form}
    return render(request, 'users_bookings/booking_edit.html', context)


@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user_id=request.user.id)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    context = {'booking': booking}
    return render(request, 'users_bookings/booking_delete.html', context)