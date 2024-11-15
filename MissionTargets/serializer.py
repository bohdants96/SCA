from rest_framework import serializers
from .models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'Name', 'Country', 'Notes', 'Complete_state']


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True, write_only=True)  # To write targets on mission creation
    targets_details = TargetSerializer(many=True, read_only=True, source='targets')  # To read related targets

    class Meta:
        model = Mission
        fields = ['id', 'Cat', 'Complete_state', 'targets', 'targets_details']

    def create(self, validated_data):
        targets_data = validated_data.pop('targets', [])

        mission = Mission.objects.create(**validated_data)

        for target_data in targets_data:
            Target.objects.create(Mission=mission, **target_data)

        return mission
