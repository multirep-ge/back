from django.http import JsonResponse
from django.views import View

from listings.models.cities import City


class CityDistrictsView(View):
    def get(self, request, *args, **kwargs):
        cities = City.objects.all()
        data = []

        for city in cities:
            city_data = {
                'city_id': city.id,  # Add city ID to the response
                'city_name': city.name,
                'districts': []
            }

            districts = city.district_set.all()
            for district in districts:
                district_data = {
                    'district_id': district.id,  # Add district ID to the response
                    'district_name': district.name
                }
                city_data['districts'].append(district_data)

            data.append(city_data)

        return JsonResponse({'cities': data})
