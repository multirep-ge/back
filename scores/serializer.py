from rest_framework import serializers

from listings.models.listings import Listing
from scores.models import Score
from users.models import MyUser


class ScoreSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Score

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        listing = validated_data.get('listing')
        existing_score = Score.objects.filter(user=user, listing=listing).first()
        if existing_score:
            self.update(existing_score, validated_data)
            return existing_score
        else:
            return super().create(validated_data)

    def validate(self, data):
        listing = data.get('listing')
        score = data.get('score')

        if score > 5 or score < 1:
            raise serializers.ValidationError('ქულა უნდა იყოს 1 და 5-ს შორის')
        if not Listing.objects.filter(id=listing.id).exists():
            raise serializers.ValidationError('განცხადების პარამეტრები არასწორია')
        return data
