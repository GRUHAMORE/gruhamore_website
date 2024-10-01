from django.shortcuts import render, redirect
from .models import Contact, Newsletter
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import NewsletterForm


def index(request):

    
    return render(request, 'index.html')

def contact(request):

     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        if name and email and subject and message:
            try:

                send_mail(
                    subject=f"Contact Form: {subject}",
                    message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                    from_email=email,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Your message was sent successfully!')
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
        else:
            messages.error(request, 'Please fill in all the fields.')

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

     return render(request, 'contact.html')

def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            return redirect('newsletter_success')  # Redirect to a success page or the same page
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
    return render(request, 'newsletter_signup.html', {'form': NewsletterForm()})


def newsletter_success(request):
    return render(request, 'newsletter_success.html')


