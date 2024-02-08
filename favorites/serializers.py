from rest_framework import serializers

from favorites.models import Favorite


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['listing']

    def validate(self, data):
        print(data.get('listing').id)
        listing_id = 4

        if listing_id is None or listing_id < 0:
            raise serializers.ValidationError({'error': 'განცხადების მისამართი არასწორადაა შეყვანილი'})

        return data
