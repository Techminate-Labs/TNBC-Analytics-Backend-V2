from rest_framework import serializers

from apis.models.contributor import Contributor

class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        exclude = ('is_active', )
