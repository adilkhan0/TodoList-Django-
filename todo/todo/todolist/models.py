from django.db import models

class task(models.Model):
    title=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
















































# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser
# )
# import uuid
# from django.core.validators import RegexValidator
# from  django.core.exceptions import ValidationError
# from django.dispatch import receiver

# # Create your models here.

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """ 
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not password:
#             raise ValueError('Users must have a password')

#         user = self.model(
#             email=self.normalize_email(email),
#         )
#         user.active=True
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_staffuser(self, email, password):
#         """
#         Creates and saves a staff user with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.staff = True
#         user.save(using=self._db)
#         return user


#     def create_superuser(self, email, password=None):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.staff=True
#         user.admin = True
#         user.save(using=self._db)
#         return user

# #---------------------------------------------USER-----------------------------------------------#
# from django.core.validators import FileExtensionValidator

# class User(AbstractBaseUser):
#     id = models.UUIDField( primary_key = True, 
#                 default = uuid.uuid4, 
#                 editable = False
#                 ) 
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     date_of_birth = models.DateField(null=True, blank=True)
#     active = models.BooleanField(default=True)
#     admin = models.BooleanField(default=False)
#     staff = models.BooleanField(default=False)
#     first_name = models.CharField(max_length=40,null=True, blank=True)
#     last_name = models.CharField(max_length=40,null=True, blank=True)
#     user_type = models.CharField(max_length=40,
#                         choices=[
#                                 ('ADMIN', 'ADMIN'),
#                                 ('DVELEOPER','DVELEOPER'),
#                                 ('PROJECT_ADMIN','PROJECT_ADMIN'),
#                                 ('USER','USER')])
#     designation=models.CharField(max_length=40,null=True, blank=True)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be entered in the format: '9999999999'. 10 digits allowed.")
#     contact_Number = models.CharField(validators=[phone_regex], max_length=10,null=True, blank=True)
#     # contact_Number=models.IntegerField(null=True, blank=True)

#     state=models.CharField(max_length=255,null=True,blank=True)

#     objects = UserManager()
#     avtar = models.FileField(upload_to='Profile/',null=True,blank=True,validators=[FileExtensionValidator(allowed_extensions=['jpeg','png','jpg'])])
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def get_full_name(self):
#         # The user is identified by their email address
#         full_name =str(self.first_name)+' '+str(self.last_name)
#         return full_name

#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.first_name

#     def __str__(self):
#         return self.email
        

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
 

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         return self.staff

#     @property
#     def is_admin(self):
#         "Is the user a admin member?"
#         return self.admin
    
#     @property
#     def is_active(self):
#         "Is the user a active member?"
#         return self.active


