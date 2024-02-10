from django.urls import path

from listings.views.cities import CityListView, CityView
from listings.views.getListings import ListingView, Filter
from listings.views.manageListings import ManageListing

urlpatterns = [
    path('ManageListing', ManageListing.as_view()),
    path('getLast8Listings', ListingView.as_view()),
    path('cities', CityListView.as_view()),
    path('', Filter.as_view()),

    path('cities/<int:city_id>', CityView.as_view()),
    path('<int:pk>',Filter.as_view() )
]
