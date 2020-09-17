
from rest_framework import serializers
from django.contrib.auth.models import User


# Loal Django Apps
from .models import Entry

class EntrySerializer(serializers.ModelSerializer):
    # user_id = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = Entry
        fields = ['user','title']
        # fields = ['name', 'email', 'password', 'age', 'semester', 'user_id', 
        #           'enroll_num', 'gender', 'hobbies', 'class_teacher', 'profile_pic']


