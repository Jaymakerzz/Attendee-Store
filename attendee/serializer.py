from django.db import transaction
from rest_framework import serializers
from .models import Attendee, Attendee_photo


class AttendeeSerializer(serializers.ModelSerializer):
    fullName = serializers.SerializerMethodField(method_name='get_full_name')
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(source='phone_number')
    photo = serializers.ImageField(source = 'photo.photo' , required=False, allow_null=True)
    class Meta:
        model = Attendee
        fields = ['id', 'firstName', 'lastName', 'fullName', 'email',
                  'phone', 'organization', 'role', 'photo']

    def get_full_name(self, attendee: Attendee):
        return f"{attendee.first_name} {attendee.last_name}"

    @transaction.atomic
    def create(self, validated_data):
        photo_data = validated_data.pop('photo', {})
        attendee = Attendee.objects.create(**validated_data)
        if photo_data.get('photo'):
            Attendee_photo.objects.create(
                attendee=attendee, photo=photo_data['photo'])
        return attendee
