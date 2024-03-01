# views.py

from rest_framework import generics

from rest_framework.response import Response

from listings.serializers import ListingSerializer


class CurrencyOptionsView(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        currency_options = serializer.fields['currency'].choices

        return Response({'currency_options': currency_options})


class TimeUnitView(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        currency_options = serializer.fields['time_unit'].choices

        return Response({'time_options': currency_options})


