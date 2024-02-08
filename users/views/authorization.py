from django.contrib.auth import authenticate, login, logout
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import RegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'message': 'მომხმარებელი წარმატებით დარეგისტრირდა',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        global email
        try:
            if 'email' not in request.data or 'password' not in request.data:
                return Response(
                    {'error': 'საჭირო ველები შესავსებია'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            email = request.data['email']
            password = request.data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                auth_data = get_tokens_for_user(request.user)
                return Response(
                    {'message': 'თქვენ წარმატებით გაიარეთ ავტორიზაცია', **auth_data, "user_id": user.id},
                    status=status.HTTP_200_OK
                )
            return Response(
                {'error': 'მონაცემები არასწორია'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except:
            return Response(
                {'error': 'შეცდომა დალოგინებისას'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(
            {'message': 'თქვენ წარმატებით გამოხვედით სისტემიდან'},
            status=status.HTTP_200_OK
        )