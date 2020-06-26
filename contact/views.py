from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you/')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'frontend/contact/contact.html', context)

def contact_messages_list(request):
    messages = Contact.objects.all()
    context = {
        'messages': messages
    }
    return render(request, 'backend/contact-messages/contact_messages_list.html', context)

def contact_message_detail(request, id):
    message = Contact.objects.get(id=id)
    # message = get_object_or_404(Contact, id = id)
    context = {
        'message': message
    }
    return render(request, 'backend/contact-messages/contact_message_detail.html', context)

def contact_message_delete(request, id):
    message = Contact.objects.get(id=id)
    message.delete()
    return redirect('/contact/messages/')
    # return render(request, 'backend/contact-messages/contact_message_delete.html')