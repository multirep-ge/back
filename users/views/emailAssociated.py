
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import EmailConfirmationToken
from users.utils import send_confirmation_email


# class UserInformation(APIView):
#     permission_classes = [IsAuthenticated, ]
#
#     def get(self, request):
#         user = request.user
#         email = user.email
#         is_email_confirmed = user.is_email_confirmed
#         payload = {'email': email, 'is_email_confirmed': is_email_confirmed}
#         return Response(data=payload, status=200)


class SendEmailConfirmation(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, format=None):
        user = request.user
        try:
            if not user.is_email_confirmed:
                user = request.user
                token = EmailConfirmationToken.objects.create(user=user)
                send_confirmation_email(email=user.email, token_id=token.pk, user_id=user.pk)
                return Response({'success': "დასტურის ბმული გამოგზავნილია თქვენს იმეილზე, გთხოვთ შეამოწმოთ"},
                                status=status.HTTP_201_CREATED)

            return Response({'message': "თქვენ უკვე ვერიფიცირებული ხართ"},
                            status=status.HTTP_202_ACCEPTED)

        except:
            return Response({'error': "შეცდომა იმეილის გამოგზავნისას, სცადეთ თავიდან"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def confirm_email_view(request):
    token_id = request.GET.get('token_id', None)
    user_id = request.GET.get('user_id', None)
    try:
        token = EmailConfirmationToken.objects.get(pk=token_id, user=user_id)
        user = token.user

        if not user.is_email_confirmed:
            user.is_email_confirmed = True
            user.save()
            data = {'is_email_confirmed': True}
            return render(request, template_name='confirm_email.html', context=data)

        if user.is_email_confirmed:
            return render(request, template_name='already_verified.html')

    except EmailConfirmationToken.DoesNotExist:
        data = {'is_email_confirmed': False}
        return render(request, template_name='confirm_email.html', context=data)
