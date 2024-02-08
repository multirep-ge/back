from django.urls import path

from favorites.views import ManageFavorites
from .views.emailAssociated import SendEmailConfirmation, confirm_email_view
from .views.authorization import RegistrationView, LoginView, LogoutView

from .views.forgotPassword import CustomResetPasswordRequestToken, SetNewPassword, GeneratePasswordResetPage
from .views.manageUsers import Me, ManageUsers, TopTenTeacher

urlpatterns = [
    path('auth/register', RegistrationView.as_view()),
    path('auth/login', LoginView.as_view()),
    path('auth/logout', LogoutView.as_view()),
    path('send-confirmation-email', SendEmailConfirmation.as_view()),
    path('confirm_email', confirm_email_view),
    path('add_to_favorites', ManageFavorites.as_view()),
    path('password_reset/', CustomResetPasswordRequestToken.as_view(), name='create_token'),
    path('password_reset/set_new_password/', SetNewPassword.as_view(), name='password_reset'),
    path('password_reset/password_reset_page/', GeneratePasswordResetPage, name='password_reset'),

    path('me', Me.as_view()),
    path('<int:pk>', ManageUsers.as_view(), name='user details'),
    path('', ManageUsers.as_view(), name='user list'),

    path('top_ten_teacher', TopTenTeacher.as_view())
]
