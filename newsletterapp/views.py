from django.shortcuts import render
# sening email directly from our views library
from django.core.mail import send_mail  
from django.conf import settings
# template loader for rendering templates inside theviews
from django.template.loader import render_to_string
from newsletterapp.models import Subscriber
# # Create your views here.
# subscription function
def subscription(request):
    if request.method =="POST":
        subscribers_email = request.POST('subscribers_email')
        
        # saving the mail
        subscriptions = subscribers_email.save()
        # rendering custom email  template
        context = {'email':subscriptions.email}
        subscriptions = Subscriber(subscription = subscription )
        
        #messages.success(request,'Your subscription request has been sent. Thank you!')
    