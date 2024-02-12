from rest_framework import permissions, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from listings.models.listings import Listing
from listings.serializers import ListingSerializer, ListingWithTeacherSerializer


class ListingView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            quantity = request.data['quantity']
            if not Listing.objects.exists():
                return Response(
                    {'error': 'განცხადებები ვერ მოიძებნა'},
                    status=status.HTTP_404_NOT_FOUND
                )
            if quantity is int:
                listings = Listing.objects.order_by('-date_created')[:quantity]
            else:
                listings = Listing.objects.order_by('-date_created')
            listings = ListingSerializer(listings, many=True, context={'request': request})
            return Response(
                {'data': listings.data},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return Response(
                {'error': 'შეცდომა ინფორმაციის მიღებისას'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ListingDetailView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        try:
            pk = int(request.data['listing_id'])
            listing = Listing.objects.get(pk=pk)
            serializer = ListingSerializer(listing, many=False, context={'request': request})
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        except Listing.DoesNotExist:
            return Response({'error': 'განცხადება ვერ მოიძებნა'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            print(e)
            return Response(
                {"message": "შეცდომა განცხადების მიღებისას"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class Filter(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, pk=None):
        if pk:
            try:
                data = Listing.objects.get(pk=pk)
                data.views += 1
                data.save()
            except:
                return Response({'error': 'განცხადება ვერ მოიძებნა'}, status.HTTP_404_NOT_FOUND)
            serializer = ListingSerializer(data,context={'request':request})
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)

        subject = self.request.query_params.get("subject")
        min_price = self.request.query_params.get("minPrice")
        max_price = self.request.query_params.get("maxPrice")
        teacher_id = self.request.query_params.get("teacher_id")

        city = self.request.query_params.get("city")
        district = self.request.query_params.get("district")
        sort_by = self.request.query_params.get("sortBy")

        queryset = Listing.objects.all()

        if teacher_id:
            queryset = queryset.filter(teacher__id=teacher_id)

        if subject:
            queryset = queryset.filter(subject__name=subject)

        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        if city:
            queryset = queryset.filter(city__name=city)
            if district:
                queryset = queryset.filter(district__name=district)

        data = ListingWithTeacherSerializer(queryset, many=True,context={'request':request}).data
        if sort_by:
            data = list(sorted(data, key=lambda x: x[sort_by]))
        paginator = PageNumberPagination()
        paginator.page_size = 12
        paginated_data = paginator.paginate_queryset(data, request)
        data = {
            'count': paginator.page.paginator.count,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'data': paginated_data
        }
        return Response(data, status.HTTP_200_OK)
