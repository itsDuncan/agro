from django import forms
from allauth.account.forms import LoginForm, SignupForm, SetPasswordForm, ResetPasswordForm, ChangePasswordForm, ResetPasswordKeyForm

class AgroLoginForm(LoginForm):

	def __init__(self, *args, **kwargs):
		super(AgroLoginForm, self).__init__(*args, **kwargs)
		for fieldname, field in self.fields.items():
			field.widget.attrs.update({
				'class': 'form-control',
			})

	def login(self, *args, **kwargs):
		return super(AgroLoginForm, self).login(*args, **kwargs)

class AgroSignupForm(SignupForm):

	def __init__(self, *args, **kwargs):
		super(AgroSignupForm, self).__init__(*args, **kwargs)
		for fieldname, field in self.fields.items():
			field.widget.attrs.update({
				'class': 'form-control',
			})

	def save(self, request):
		user = super(AgroSignupForm, self).save(request)

		return user

class AgroResetPasswordForm(ResetPasswordForm):

	def __init__(self, *args, **kwargs):
		super(AgroResetPasswordForm, self).__init__(*args, **kwargs)
		for fieldname, field in self.fields.items():
			field.widget.attrs.update({
				'class': 'form-control',
			})

	def save(self, request):
		email_address = super(AgroResetPasswordForm, self).save(request)

		return email_address

class AgroSetPasswordForm(SetPasswordForm):

	def __init__(self, *args, **kwargs):
		super(AgroSetPasswordForm, self).__init__(*args, **kwargs)
		for fieldname, field in self.fields.items():
			field.widget.attrs.update({
				'class': 'form-control',
			})

	def save(self):
		super(AgroSetPasswordForm, self).save()

class AgroResetPasswordKeyForm(ResetPasswordKeyForm):

	def __init__(self, *args, **kwargs):
		super(AgroResetPasswordKeyForm, self).__init__(*args, **kwargs)
		for fieldname, field in self.fields.items():
			field.widget.attrs.update({
				'class': 'form-control',
			})

	def save(self):
		super(AgroResetPasswordKeyForm, self).save()

class AgroChangePasswordForm(ChangePasswordForm):

	def __init__(self, *args, **kwargs):
		super(AgroChangePasswordForm, self).__init__(*args, **kwargs)
		for fieldname, field in self.fields.items():
			field.widget.attrs.update({
				'class': 'form-control',
			})