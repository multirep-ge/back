from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from favorites.models import Favorite
from favorites.serializers import FavoritesSerializer
from listings.models.listings import Listing


class ManageFavorites(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = FavoritesSerializer(data=request.data)
            if serializer.is_valid():
                user = request.user
                listing_id = serializer.validated_data['listing'].id

                try:
                    listing = Listing.objects.get(id=listing_id)
                except Listing.DoesNotExist:
                    return Response({'error': 'განცხადება ვერ მოიძებნა'}, status=status.HTTP_404_NOT_FOUND)
                Favorite.objects.create(user=user, listing=listing)
                return Response({'success': 'განცხადება დაემატა ფავორიტებში'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "განცხადება უკვე დამატებულია ფავორიტებში"})

    def delete(self, request, format=None):
        try:
            ID = request.data.get('listing')
            user = request.user
            if not Favorite.objects.filter(user=user.id, listing_id=ID).exists():
                return Response(
                    {'error': "ეს განცხადება არაა თქვენს ფავორიტებში"},
                    status=status.HTTP_404_NOT_FOUND
                )
            Favorite.objects.filter(user=user.id, listing_id=ID).delete()

            if not Favorite.objects.filter(user=user.id, listing_id=ID).exists():
                return Response(
                    status=status.HTTP_204_NO_CONTENT
                )
            else:
                return Response(
                    {'error': "განცხადება ვერ წაიშალა"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as a:
            return Response(
                {'error': 'შეცდომა განცხადების წაშლისას'},

                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
