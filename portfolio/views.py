from django.shortcuts import render
from django.shortcuts import render, redirect

# standard views #
from .forms import BookingRequestForm, ContactRequestForm
from django.contrib import messages

# for form submissions #
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, 'portfolio/kylieportfolio.html')

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

def booking_request_view(request):
    if request.method == 'POST':
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            booking = form.save()  # Save booking to the database

            # Send email notification
            send_mail(
                subject=f'New Booking Request from {booking.name}',
                message=f'''
                Thank you for booking a shoot you little whore!
                

                Booking Details:
                Name: {booking.name} the whore
                Email: {booking.email}
                Phone: {booking.phone}
                Date: {booking.date}
                Session Type: Nude {booking.session_type}
                Details: {booking.details}
                ''',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[f'{booking.email}'],  # Change this to the recipient email
                fail_silently=False,
            )
            # Send email notification
            send_mail(
                subject=f'New Booking Request from {booking.name}',
                message=f'''
                Thank you for booking a shoot you little whore!
                

                Booking Details:
                Name: {booking.name} the whore
                Email: {booking.email}
                Phone: {booking.phone}
                Date: {booking.date}
                Session Type: Nude {booking.session_type}
                Details: {booking.details}
                ''',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[f'ethansmasters@outlook.com'],  # Change this to the recipient email
                fail_silently=False,
            )

            messages.success(request, 'Your booking request has been submitted and an email has been sent!')
            return redirect('booking')
    else:
        form = BookingRequestForm()

    return render(request, 'portfolio/booking.html', {'form': form})

def contact_request_view(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            contact = form.save()  # Save contact to the database

            # Send email notification
            send_mail(
                subject=f'New Contact Message from {contact.name}',
                message=f'''
                Contact Message:
                Name: {contact.name}
                Email: {contact.email}
                Message: {contact.message}
                ''',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[f'{contact.email}'],  # Change this to the recipient email
                fail_silently=False,
            )

            send_mail(
                subject=f'New Contact Message from {contact.name}',
                message=f'''
                Contact Message:
                Name: {contact.name}
                Email: {contact.email}
                Message: {contact.message}
                ''',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['ethansmasters@outlook.com'],  # Change this to the recipient email
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent and an email has been sent!')
            return redirect('contact')
    else:
        form = ContactRequestForm()

    return render(request, 'portfolio/contact.html', {'form': form})
