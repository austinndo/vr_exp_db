from rest_framework import serializers
from .models import Experience


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    experience = serializers.HyperlinkedRelatedField(
        view_name='experience_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Experience
        fields = ('user_age', 'headset_type', 'duration_of_use',
                  'motion_sickness', 'immersion_level')
