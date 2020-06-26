from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Partner
from .forms import PartnerForm


# class PartnersView(ListView):
#     model = Partner
#     context_object_name = "partners"
#     template_name = "backend/partners/partners.html"

def partners_view(request):
    partners = Partner.objects.all()        
    context = {
        'partners': partners
    }
    return render(request, 'backend/partners/partners.html', context)

def partner_list_view(request):
    partners = Partner.objects.all()        
    context = {
        'partners': partners
    }
    return render(request, 'backend/partners/partner-list.html', context)

def partner_detail_view(request, id):
    partner = Partner.objects.get(id=id)
    context = {
        'partner': partner
    }
    return render(request, 'backend/partners/partner-detail.html', context)

def partner_create_view(request):
    if request.method == "POST":
        form = PartnerForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/partners/list/')
    else:
        form = PartnerForm()
    context = {
        'form': form
    }
    return render(request, 'backend/partners/partner-create.html', context)

def partner_update_view(request, id):
    instance = get_object_or_404(Partner, id=id)
    form = PartnerForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/partners/list/')
    
    context = {
        'form': form
    }
    return render(request, 'backend/partners/partner-update.html', context)

class partner_delete_view(DeleteView):
    model = Partner
    template_name = 'backend/partners/partner-delete.html'
    success_url = reverse_lazy('partner-list')
    # partner = Partner.objects.get(id=id)
    # partner.delete()
    # return redirect('/partner/list/')