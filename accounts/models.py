from django.db import models
from django.urls import reverse
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfileManager(BaseUserManager):
	use_in_migrations = True

	def create_user(self, email, username, password=None, **extra_fields):

		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password=None, **extra_fields):

		user = self.create_user(
			email,
			password=password,
			username=username,
		)
		user.is_admin = True

		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
	)

	username = models.CharField(
		unique=True,
		max_length=50
	)

	firstname = models.CharField(
		max_length=50,
		blank=True,
		null=True
	)

	lastname = models.CharField(
		max_length=50,
		blank=True,
		null=True
	)

	profile_picture = models.ImageField(
		upload_to = 'media/profile_picture/',
		blank = True,
		null = True,
	)

	phone_number = models.CharField(
		max_length=30,
		blank=True,
		null=True
	)

	description = models.TextField(
		blank=True,
		null=True,
		help_text='Tell us something about yourself'
	)

	wholesaler = models.BooleanField(
		default = False,
	)

	@property
	def is_wholesaler(self):
		return self.wholesaler

	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = UserProfileManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def __str__(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin

	def get_absolute_url(self):
		return reverse('profile', args[str(self.username)])

@receiver(post_save, sender=User)
def user_profile_postsave(sender, instance, created, *args, **kwargs):
	if instance.is_wholesaler:
		SupplierProfile.objects.get_or_create(user=instance)