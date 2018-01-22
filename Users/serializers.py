from rest_framework import serializers
from Users.models import *

class SerializerUserInformation(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = ("id", "user_name", "user_password", "face_photo_url", "join_time", "is_guide", "is_certified", "is_certified_guide")
    # id = serializers.IntegerField(read_only=True)
    # user_name = serializers.CharField(max_length = 20,required=True, allow_blank=False)
    # user_password  = serializers.CharField(max_length=16,required=True, allow_blank=False)
    # face_photo_url = serializers.CharField(required = False, max_length=400, allow_blank=True)
    # join_time = serializers.DateTimeField(required = False)
    # is_guide = serializers.BooleanField(required = False)
    # is_certified = serializers.BooleanField(required = False)
    # is_certified_guide = serializers.BooleanField(required = False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return UserInformation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.user_password = validated_data.get('user_password', instance.user_password)
        instance.face_photo_url = validated_data.get('face_photo_url', instance.face_photo_url)
        instance.join_time = validated_data.get('join_time', instance.join_time)
        instance.is_guide = validated_data.get('is_guide', instance.is_guide)
        instance.is_certified = validated_data.get('is_certified', instance.is_certified)
        instance.is_certified_guide = validated_data.get('is_certified_guide', instance.is_certified_guide)
        instance.save()
        return instance

class SerializerUserContact(serializers.ModelSerializer):
    user = SerializerUserInformation(required=False)
    class Meta:
        model = UserContact
        fields = ("user", "user_phone", "user_email", "user_wechat", "user_whatsapp")

    def update(self, instance, validated_data):
        # user_data = validated_data.pop('user')
        # users = SerializerUserInformation(data = user_data)
        # users.is_valid()
        # user = users.create(users.validated_data)
        instance.user_phone = validated_data.get('user_phone', instance.user_phone)
        instance.user_email = validated_data.get('user_email', instance.user_email)
        instance.user_wechat = validated_data.get('user_wechat', instance.user_wechat)
        instance.user_whatsapp = validated_data.get('user_whatsapp', instance.user_whatsapp)
        instance.save()
        return instance

class SerializerUserBackground(serializers.ModelSerializer):
    user = SerializerUserInformation(required=False)
    class Meta:
        model = UserBackground
        fields = ("user", "user_gender", "user_home_country", "user_home_province",
                  "user_home_city", "user_now_country", "user_now_province", "user_now_city", "user_time")

    def update(self, instance, validated_data):
        instance.user_gender = validated_data.get("user_gender", instance.user_gender)
        instance.user_home_country = validated_data.get("user_home_country", instance.user_home_country)
        instance.user_home_province = validated_data.get("user_home_province", instance.user_home_province)
        instance.user_home_city = validated_data.get("user_home_city", instance.user_home_city)
        instance.user_now_country = validated_data.get("user_now_country", instance.user_now_country)
        instance.user_now_province = validated_data.get("user_now_province", instance.user_now_province)
        instance.user_now_city = validated_data.get("user_now_city", instance.user_now_city)
        instance.user_time = validated_data.get("user_time", instance.user_time)
        instance.save()
        return instance

class SerializerUserEducation(serializers.ModelSerializer):
    user = SerializerUserInformation(required=False)
    class Meta:
        model = UserEducation
        fields = ("user", "user_degree", "user_school", "user_major")

    def update(self, instance, validated_data):
        instance.user_degree = validated_data.get("user_degree", instance.user_degree)
        instance.user_school = validated_data.get("user_school", instance.user_school)
        instance.user_major = validated_data.get("user_major", instance.user_major)
        instance.save()
        return instance

class SerializerUserGuide(serializers.ModelSerializer):
    user = SerializerUserInformation(required=False)
    class Meta:
        model = UserGuide
        fields = ("user", "certified_guide", "guide_certification_url", "car_photo_url", "car_plate_number", "start_time")

    def update(self, instance, validated_data):
        instance.certified_guide = validated_data.get("certified_guide", instance.certified_guide)
        instance.guide_certification_url = validated_data.get("guide_certification_url", instance.guide_certification_url)
        instance.car_photo_url = validated_data.get("car_photo_url", instance.car_photo_url)
        instance.car_plate_number = validated_data.get("car_plate_number", instance.car_plate_number)
        instance.start_time = validated_data.get("start_time", instance.start_time)
        instance.save()
        return instance

class SerializerUserIdentity(serializers.ModelSerializer):
    user = SerializerUserInformation(required=False)
    class Meta:
        model = UserIdentity
        fields = ("user", "user_passport", "passport_photo_url", "passport_issued_country", "user_identity", "identity_photo_url",
                  "identity_issued_country")

    def update(self, instance, validated_data):
        instance.user_passport = validated_data.get("user_passport", instance.user_passport)
        instance.passport_photo_url = validated_data.get("passport_photo_url", instance.passport_photo_url)
        instance.passport_issued_country = validated_data.get("passport_issued_country", instance.passport_issued_country)
        instance.user_identity = validated_data.get("user_identity", instance.user_identity)
        instance.identity_photo_url = validated_data.get("identity_photo_url", instance.identity_photo_url)
        instance.identity_issued_country = validated_data.get("identity_issued_country", instance.identity_issued_country)
        instance.save()
        return instance


class SerializerUserLanguage(serializers.ModelSerializer):
    user = SerializerUserInformation(required=False)
    class Meta:
        model = UserLanguage
        fields = ("user", "user_language1", "user_skill1", "user_language2", "user_skill2", "user_language3", "user_skill3")

    def update(self, instance, validated_data):
        instance.user_language1 = validated_data.get("user_language1", instance.user_language1)
        instance.user_skill1 = validated_data.get("user_skill1", instance.user_skill1)
        instance.user_language2 = validated_data.get("user_language2", instance.user_language2)
        instance.user_skill2 = validated_data.get("user_skill2", instance.user_skill2)
        instance.user_language3 = validated_data.get("user_language3", instance.user_language3)
        instance.user_skill3 = validated_data.get("user_skill3", instance.user_skill3)
        instance.save()
        return instance