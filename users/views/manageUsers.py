from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import MyUser
from users.serializers import ProfileSerializer


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            data = request.user
            serializer = ProfileSerializer(data)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'გაუთვალისწინებელი ხარვეზი'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ManageUsers(APIView):

    def get(self, request, pk=None):
        try:
            if pk:
                try:
                    data = MyUser.objects.get(pk=pk)
                except:
                    return Response({'error': 'მომხმარებელი ვერ მოიძებნა'}, status.HTTP_404_NOT_FOUND)
                serializer = ProfileSerializer(data)
                return Response({'data': serializer.data}, status=status.HTTP_200_OK)

            paginator = PageNumberPagination()
            paginator.page_size = 12
            queryset = MyUser.objects.all().order_by('id')
            paginated_data = paginator.paginate_queryset(queryset, request)
            serializer = ProfileSerializer(paginated_data, many=True)

            data = {
                'count': paginator.page.paginator.count,
                'next': paginator.get_next_link(),
                'previous': paginator.get_previous_link(),
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'გაუთვალისწინებელი ხარვეზი'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk=None):
        try:
            try:
                instance = MyUser.objects.get(pk=pk)
            except:
                return Response({'error': 'მომხმარებელი ვერ მოიძებნა'}, status.HTTP_404_NOT_FOUND)
            if instance != request.user:
                return Response({'error': 'არ გაქვს მონაცემების შეცვლის უფლება'}, status.HTTP_403_FORBIDDEN)

            serializer = ProfileSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'message': 'მომხმარებელის ინფორმაცია წარმატებით განახლდა',
                        'data': serializer.data
                    },
                    status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'გაუთვალისწინებელი ხარვეზი'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TopTenTeacher(APIView):
    def get(self, request):
        try:
            data = MyUser.objects.filter(is_teacher=True)
            serializer = ProfileSerializer(data, many=True)

            top_ten = sorted(serializer.data, key=lambda x: x['average_teacher_score'], reverse=True)[:10]

            return Response({'data': top_ten}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'გაუთვალისწინებელი ხარვეზი'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
