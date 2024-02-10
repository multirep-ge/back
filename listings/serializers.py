from rest_framework import serializers

from listings.models.cities import City
from listings.models.districts import District
from listings.models.listings import Listing
from testuni.settings import BASE_URL


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class DistrictSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = District
        fields = ('id', 'name', 'city')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('city', None)
        return representation


class ListingSerializer(serializers.ModelSerializer):
    _photo = serializers.SerializerMethodField()
    _city = serializers.SerializerMethodField()
    _district = serializers.SerializerMethodField()
    _subject = serializers.SerializerMethodField()
    average_listing_score = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = (
            'id', 'title', 'teacher', 'description', 'price',
            'city', 'district', 'subject', 'photo',
            '_city', '_district', '_subject','_photo',
            'date_created', 'views', 'average_listing_score'
        )

        extra_kwargs = {
            'city': {'write_only': True},
            'district': {'write_only': True},
            'subject': {'write_only': True},
            'photo': {'write_only': True}
        }

    def get__photo(self, obj):
        if obj.photo:
            return self.context.get('request').build_absolute_uri(obj.photo.url)
        return None

    def get__city(self, obj):
        if obj.city:
            return obj.city.name

    def get__district(self, obj):
        if obj.district:
            return obj.district.name

    def get__subject(self, obj):
        if obj.subject:
            return obj.subject.name

    def get_average_listing_score(self, obj):
        if obj.average_listing_score:
            return round(obj.average_listing_score, 2)
        return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'city' in representation and representation['city'] is None:
            representation.pop('city')
        if 'district' in representation and representation['district'] is None:
            representation.pop('district')
        return representation

    def validate(self, data):

        price = data.get('price')
        errors = []
        district = data.get('district')
        city = data.get('city')
        if district is not None and city is not None and district.city != city:
            raise serializers.ValidationError({'error': 'District does not belong to the specified city'})

        if price < 0:
            errors.append('ფასი უნდა იყოს დადებითი რიცხვი')
        if len(errors) > 0:
            raise serializers.ValidationError({'errors': errors})

        return data

    def create(self, validated_data):
        user = self.context['request'].user

        # Check if the user has the 'teacher' attribute
        if hasattr(user, 'teacher'):
            teacher = user.teacher
            validated_data['teacher'] = teacher
            listing = Listing.objects.create(**validated_data)
            return listing
        else:
            raise serializers.ValidationError({'error': 'User does not have a teacher attribute'})


class EditListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'price', 'city', 'district', 'subject', 'photo')
        partial = True

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'city' in representation and representation['city'] is None:
            representation.pop('city')
        if 'district' in representation and representation['district'] is None:
            representation.pop('district')
        return representation

    def validate(self, data):
        price = data.get('price')
        errors = []
        district = data.get('district')
        city = data.get('city')
        if district is not None and city is not None and district.city != city:
            raise serializers.ValidationError({'error': 'ეს უბანი მითითებულ ქალაქს არ ეკუთვნის'})

        if price and price < 0:
            errors.append('ფასი უნდა იყოს დადებითი რიცხვი')

        if len(errors) > 0:
            raise serializers.ValidationError({'errors': errors})

        return data
