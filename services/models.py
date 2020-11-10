from django.db import models
from django.conf import settings
from django.db.models.signals import m2m_changed
from django.utils.text import slugify

class ServiceCartManager(models.Manager):

	def new_or_get(self, request):
		cart_id = request.session.get("cart_id", None)

		qs = self.get_queryset().filter(id=cart_id)
		if qs.count() == 1:
			new_obj = False
			cart = qs.first()
			if request.user.is_authenticated and cart.user is None:
				cart.user = request.user
				cart.save()
		else:
			cart = self.new(user=request.user)
			new_obj = True
			request.session['cart_id'] = cart.id

		return cart, new_obj

	def new(self, user=None):
		user_obj = None
		if user is not None:
			if user.is_authenticated:
				user_obj = user
		return self.model.objects.create(user=user_obj)

	def delete_blank(self):
		return self.model.objects.get_queryset().filter(services=None).delete()

class Service(models.Model):
	service_id = models.SlugField(unique=True, blank=True, null=True)
	name = models.CharField(unique=True, max_length=50)
	description = models.TextField()
	suppliers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='supplier')
	unit_of_measure = models.CharField(max_length=20)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	cost = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, blank=True)

	def __str__(self):
		return str(self.service_id)

	def save(self, *args, **kwargs):
		self.service_id = slugify(self.name)
		super().save(*args, **kwargs)

class Category(models.Model):
	category_id = models.SlugField(unique=True)
	name = models.CharField(unique=True, max_length=50)
	description = models.TextField()
	services = models.ManyToManyField(Service, blank=True, related_name='services')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.category_id

class ServiceCart(models.Model):
	tag_name = models.CharField(max_length=50, blank=True, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
	services = models.ManyToManyField(Service, blank=True)
	created = models.DateTimeField(auto_now_add=True)

	status = models.CharField(max_length=25, blank=True, null=True)
	suppliers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='suppliers', blank=True)
	location = models.CharField(max_length=50, default='Nairobi')
	sub_total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
	total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
	modified = models.DateTimeField(auto_now=True)
	expiry = models.DateTimeField(null=True, blank=True)

	objects = ServiceCartManager()

	def __str__(self):
		return str(self.id)

def m2m_service_cart_receiver(sender, instance, action, *args, **kwargs):

	if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
		services = instance.services.all()
		instance.save()

m2m_changed.connect(m2m_service_cart_receiver, sender=ServiceCart.services.through)
	