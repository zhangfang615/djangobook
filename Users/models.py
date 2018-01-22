from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class UserInformation(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length = 20,blank=False)
    user_password  = models.CharField(max_length=16,blank=False)
    face_photo_url = models.CharField(max_length=400, blank=True)
    join_time = models.DateTimeField(auto_now_add= True)
    is_guide = models.BooleanField(blank=False, default=False)
    is_certified = models.BooleanField(blank=False, default=False)
    is_certified_guide = models.BooleanField(blank=False, default=False)

    def __unicode__(self):
        return self.user_name

class UserContact(models.Model):
    user = models.OneToOneField(UserInformation,on_delete=models.CASCADE, primary_key=True)
    user_phone = models.CharField(max_length=20, blank=True)
    user_email = models.EmailField(blank=True)
    user_wechat = models.CharField(max_length=20, blank=True)
    user_whatsapp = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return self.user_phone

class UserBackground(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
        (u'NA', u'Not sure')
    )
    user = models.OneToOneField(UserInformation, on_delete=models.CASCADE, primary_key=True)
    user_gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank = True)
    user_home_country = models.CharField(max_length=30, blank = True)
    user_home_province = models.CharField(max_length=30, blank=True)
    user_home_city = models.CharField(max_length=30, blank=True)
    user_now_country = models.CharField(max_length=30, blank=True)
    user_now_province = models.CharField(max_length=30, blank=True)
    user_now_city = models.CharField(max_length=30, blank=True)
    user_time = models.IntegerField(
        validators=[
            MaxValueValidator(50),
            MinValueValidator(1)
        ],
        blank=True,
        default=1
    )

    def __unicode__(self):
        return self.user.user_name



class UserEducation(models.Model):
    degree_choices = (
        (u'El', u'Elementary'),
        (u'Se', u'Secondary'),
        (u'Ba', u'Bachelor'),
        (u'Ma', u'Master'),
        (u'DC', u'Doctor'),
        (u'PD', u'Post Doctor')
    )
    user = models.OneToOneField(UserInformation, on_delete=models.CASCADE, primary_key=True)
    user_degree = models.CharField(max_length=2, choices=degree_choices, blank=True)
    user_school = models.CharField(max_length=50, blank=True)
    user_major = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return self.user.user_name

class UserLanguage(models.Model):
    user = models.OneToOneField(UserInformation, on_delete=models.CASCADE, primary_key=True)
    skill_choices = {
        (u'M', u'Mother Tougne'),
        (u'B', u'Beginning'),
        (u'L', u'Limilted'),
        (u'I', u'Influent'),
        (u'P', u'Proficient')
    }
    user_language1 = models.CharField(max_length=20, blank=True)
    user_skill1 = models.CharField(max_length=1, choices=skill_choices, blank=True)
    user_language2 = models.CharField(max_length=20, blank=True)
    user_skill2 = models.CharField(max_length=1, choices=skill_choices, blank=True)
    user_language3 = models.CharField(max_length=20, blank=True)
    user_skill3 = models.CharField(max_length=1, choices=skill_choices, blank=True)

    def __unicode__(self):
        return self.user.user_name


class UserIdentity(models.Model):
    user = models.OneToOneField(UserInformation, on_delete=models.CASCADE, primary_key=True)
    user_passport = models.CharField(max_length=15, blank=True)
    passport_photo_url = models.CharField(max_length=400, blank=True)
    passport_issued_country = models.CharField(max_length=30, blank=True)
    user_identity = models.CharField(max_length=20, blank=True)
    identity_photo_url = models.CharField(max_length=400, blank=True)
    identity_issued_country = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.user.user_name

class UserGuide(models.Model):
    user = models.OneToOneField(UserInformation, on_delete=models.CASCADE, primary_key=True)
    certified_guide = models.BooleanField(blank=False, default=False)
    guide_certification_url = models.CharField(max_length=400, blank=True)
    car_photo_url = models.CharField(max_length=400, blank=True)
    car_plate_number = models.CharField(max_length=10, blank=True)
    start_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.user.user_name

@receiver(post_save, sender=UserInformation)
def create_User(sender, instance, created, **kwargs):
    if created:
        UserContact.objects.create(user=instance)
        UserBackground.objects.create(user=instance)
        UserEducation.objects.create(user=instance)
        UserLanguage.objects.create(user=instance)
        UserIdentity.objects.create(user=instance)
        UserGuide.objects.create(user=instance)

