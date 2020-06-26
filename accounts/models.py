from django.db import models
from django.urls import reverse
from django.conf import settings
# from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# class Designation(models.Model):
# 	title = models.CharField(max_length=50, unique=True)
	
# 	class Meta:
# 		ordering = ('title', )
	
# 	def __str__(self):
# 		return self.title
	
	


class Profile(models.Model):
	DESIGNATION_CHOICES = (
			('chm', 'Chairman'),
			('vchm', 'Vice Chairman'),
			('sec', 'Secretary'),
			('fsec', 'Financial Secretary'),
			('asec', 'Assistant Secretary'),
			('tre', 'Treasurer'),
			('osec', 'Organising Secretary'),
			('aosec', 'Assistant Organising Secretary'),
			('legal', 'Legal Adviser'),
			('aud1', 'Auditor I'),
			('aud2', 'Auditor II'),
			('pro1', 'PRO I'),
			('pro2', 'PRO II'),
			('ylead', 'Youth Leader'),
			('wlead', 'Women Leader'),
			('dcoord', 'District Coordinator'),
			('mem', 'Member'),
		)
	QUALIFICATION_CHOICES = (
			('phd', 'PhD'), ('msc', 'Masters'), ('deg', 'Degree'), ('hnd', 'HND'),
			('nce', 'NCE'), ('diploma', 'Diploma'),	('ssce', 'SSCE'), ('pri', 'Primary'),
			('others', 'Others')
		)
	STATE_CHOICES = (
			('abia', 'Abia'), ('adamawa', 'Adamawa'), ('akwaibom', 'Akwa Ibom'),
			('anambra', 'Anambra'),
			('bauchi', 'Bauchi'),
			('bayelsa', 'Bayelsa'),
			('benue', 'Benue'), ('borno', 'Borno'), ('cr', 'Cross River'),
			('belta', 'Delta'), ('edo', 'Edo'), ('enugu', 'Enugu'), ('gombe', 'Gombe'),
			('imo', 'Imo'),	('jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('kano', 'Kano'),
			('katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'),('kwara', 'Kwara'),
			('niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('osun', 'Osun'),
			('oyo', 'Oyo'), ('tlateau', 'Plateau'),	('Rivers', 'Rivers'), ('sokoto', 'Sokoto'),
			('taraba', 'Taraba'), ('Yobe', 'Yobe'), ('zamfara', 'Zamfara'), ('fct', 'FCT'),
		)
	BAUCHI_LGA_CHOICES = (
			('Alkaleri', 'Alkaleri'), ('Bauchi', 'Bauchi'), ('Bogoro', 'Bogoro'),('Dambam', 'Dambam'),
			('Darazo', 'Darazo'), ('Dass', 'Dass'), ('Gamawa', 'Gamawa'), ('Ganjuwa', 'Ganjuwa'),
			('Giade', 'Giade'), ('Itas gadau', 'Itas gadau'), ('Jamaare', 'Jamaare'), ('Katagum', 'Katagum'),
			('Kirfi', 'Kirfi'), ('Misau', 'Misau'), ('Ningi', 'Ningi'), ('Shira', 'Shira'),
			('Tafawa Balewa', 'Tafawa Balewa'), ('Toro', 'Toro'), ('Warji', 'Warji'), ('Zaki', 'Zaki')
		)
	DISTRICT_CHOICES = (
			('Jamaa', 'Jama\'a District'), ('Toro District', 'Toro District'), ('Lame District', 'Lame District')
		)
	WARD_CHOICES = (
			('Toro', 'Toro'), ('Tilde', 'Tilde'),
			('Ribina West', 'Ribina West'), ('Ribina East', 'Ribina East'),
			('Tulai', 'Tulai'), ('Mara', 'Mara'), ('Palama', 'Palama'),
			('Jamaa', 'Jama\'a'), ('Zaranda', 'Zaranda'), ('Rauta geji', 'Rauta geji'),
			('Wonu South', 'Wonu South'), ('Wonu North', 'Wonu North'), ('Rishi', 'Rishi'),
			('Zalau', 'Zalau'), ('Rahama', 'Rahama'), ('Tama', 'Tama'), ('Lame', 'Lame'),
		)
	SENATORIAL_DISTRICT_CHOICES = (
			('Bauchi South', 'Bauchi South'), ('Bauchi Central', 'Bauchi Central'), ('Bauchi North', 'Bauchi North')
		)
	GENDER_CHOICES = (('Female', 'Female'), ('Male', 'Male'))
	user = models.OneToOneField(settings.AUTH_USER_MODEL, unique = True, on_delete = models.CASCADE)
	member_id = models.CharField(max_length=10, unique=True)
	picture = models.ImageField(upload_to = 'profiles/', null = True, blank = True)
	qualification = models.CharField(max_length = 10, choices = QUALIFICATION_CHOICES, default = '', null = True, blank = True)
	# designation   = models.ForeignKey(Designation, on_delete=models.CASCADE, null=True, blank = True)
	designation = models.CharField(max_length = 50, choices = DESIGNATION_CHOICES, default = 'mem', null = True, blank = True)
	occupation = models.CharField(max_length = 100, default = '', null = True, blank = True)
	gender = models.CharField(max_length = 6, choices = GENDER_CHOICES, default = '', null = True, blank = True)
	phone = models.PositiveIntegerField(default = 0, unique =True, null = True, blank = True)
	state = models.CharField(max_length = 20, choices = STATE_CHOICES, default = 'Bauchi', null = True, blank = True)
	senatorial_district = models.CharField(max_length = 20, choices = SENATORIAL_DISTRICT_CHOICES, default = '', null = True, blank = True)
	local_government = models.CharField(max_length = 20, choices = BAUCHI_LGA_CHOICES, default = 'Toro', null = True, blank = True)
	district = models.CharField(max_length = 20, choices = DISTRICT_CHOICES, default = '', null = True, blank = True)
	ward = models.CharField(max_length = 20, choices = WARD_CHOICES, default = '', null = True, blank = True)
	street = models.CharField(max_length = 120, default = '', null = True, blank = True)
	house_no = models.CharField(max_length = 30)
	about = models.TextField(null = True, blank = True, help_text = 'Write a little about yourself')

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_or_update_user_profle(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user = instance)
	instance.profile.save()