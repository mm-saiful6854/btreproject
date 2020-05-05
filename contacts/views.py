from django.shortcuts import render,redirect

from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    if request.method == 'POST':
        u_id = request.POST['user_id']
        list_id = request.POST['listing_id']
        realtor_email = request.POST['realtor_email']
        listing =  request.POST['listing']
        name  = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if(request.user.is_authenticated):
            u_id= request.user.id
            has_contact = Contact.objects.all().filter(user_id=u_id,listing_id=list_id)
            if(has_contact):
                messages.error(request,'You have already enquired')
                return redirect('/listings/'+list_id)

        contact = Contact(listing_id = list_id, listing=listing,name=name,email=email,phone=phone, message=message,user_id=u_id)

        contact.save()

        # send email: 

        '''send_mail(
            'property listing inquiry',
            'There has been an inquiry for' + listing + '. Sign into admin panel for more info.',
            'from@example.com',
            [realtor_email],
            fail_silently = False,
        )'''


        messages.success(request,'enquire submitted, realtor will contact as soon as possible')

        return redirect('/listings/'+list_id)