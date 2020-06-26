from django.shortcuts import render, redirect
from partner.models import Partner
from .models import FaqQuestion, FaqAnswer
from .forms import FaqForm
from blog.models import Post
from portfolio.models import Project
from django.contrib.auth.models import User


def index(request):
    user_count = User.objects.count()
    partners = Partner.objects.all()
    partner_count = Partner.objects.count()
    project_count = Project.objects.count()
    projects = Project.objects.filter(completed=True)
    recent_posts = Post.objects.order_by('-created')[:3]
    context = {
        'partners': partners,
        'partner_count': partner_count,
        'project_count': project_count,
        'projects': projects,
        'recent_posts': recent_posts,
        'user_count': user_count
    }
    return render(request, 'frontend/index.html', context)

def about(request):
    user_count = User.objects.count()
    partners = Partner.objects.all()
    partner_count = Partner.objects.count()
    project_count = Project.objects.count()
    # users = User.objects.all()
    users = User.objects.filter(is_active=True)

    context = {
        'partners': partners,
        'partner_count': partner_count,
        'project_count': project_count,
        # 'recent_posts': recent_posts,
        'user_count': user_count,
        'users': users
    }
    return render(request, 'frontend/about.html', context)

def faq(request):
    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/faqs/')
    else:
        form = FaqForm()
    answers = FaqAnswer.objects.all()
    context = {
        'form': form,
        'answers': answers
    }
    return render(request, 'frontend/faq.html', context)


def privacy_policy(request):
    return render(request, 'frontend/privacy-policy.html')

def terms_and_conditions(request):
    return render(request, 'frontend/terms-and-conditions.html')

def thank_you(request):
    return render(request, 'frontend/thank-you.html')