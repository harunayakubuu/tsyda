from django.shortcuts import render, redirect
from . models import Profile
from django.shortcuts import get_object_or_404
from . forms import UserEditForm, ProfileEditForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from portfolio.models import Project
from partner.models import Partner


@login_required
def dashboard(request):
	users = User.objects.count()
	# portfolios = Portfolio.objects.count()
	context = {
		'users': users,
		# 'portfolios': portfolios
	}
	return render(request, 'backend/dashboard.html', context)

@login_required
def user_list(request):
	users = User.objects.filter(is_active=True)

	context = {
		'section': 'people',
		'users': users
	}
	return render(request, 'backend/users/user_list.html', context)

@login_required
def user_detail(request, username):
	user = get_object_or_404(User, username=username, is_active=True)
	context = {
		'section': 'people', 
		'user': user
	}
	return render(request, 'backend/users/user_detail.html', context)


@login_required
def profile(request):
	
	context = {
		# 'members': members
	}
	return render(request, 'backend/users/profile.html', context)


@login_required
def profile_update(request):
	if request.method == "POST":
		user_form = UserEditForm(request.POST, instance = request.user)
		profile_form = ProfileEditForm(request.POST, request.FILES or None, instance= request.user.profile)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			# messages.success(request, ("Your Profile is updated successfully"))
			return redirect('/accounts/profile/')
		# else:
		# 	messages.error(request, ('please correct the error'))
	else:
		user_form = UserEditForm(instance = request.user)
		profile_form = ProfileEditForm(instance = request.user.profile)

	context = {
		"user_form": user_form,
		"profile_form": profile_form
	}
	return render(request, 'backend/users/profile_update.html', context)