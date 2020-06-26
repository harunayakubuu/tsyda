from django.contrib import admin
from . models import Profile#, Designation
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

#Register your models here.
# admin.site.register(Designation)

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'Profiles'
	fk_name = 'user'

class ProfileAdmin(UserAdmin):
	inlines = (ProfileInline, )
	list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_designation')
	list_select_related = ('profile', )

	def get_designation(self, instance):
		return instance.profile.designation
	get_designation.short_description = 'Designation'

	def get_inline_instances(self, request, obj = None):
		if not obj:
			return list()
		return super(ProfileAdmin, self).get_inline_instances(request, obj)
admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)