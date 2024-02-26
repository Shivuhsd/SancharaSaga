from rest_framework import serializers

from . models import BookingUser, Feedback

class SerializedBooking(serializers.ModelSerializer):
    class Meta:
        model = BookingUser
        fields = [
            'name',
            'date',
            'email',
            'peoples',
            'whats_app_num',
            'pick_up_point',
        ]


class SerializedFeedback(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = [
            'name',
            'phone',
            'message',
        ]