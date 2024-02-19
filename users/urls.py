from django.urls import path

from .views.authorization import RegistrationView, LoginView, LogoutView, VerifyOTP, CheckTokenView
from .views.favorites import AddToFavoritesView, RemoveFromFavoritesView, GetAllFavoritesOfUser

from .views.forgotPassword import CustomResetPasswordRequestToken, SetNewPassword
from .views.manageUsers import Me, ManageUsers, TopTenTeacher, check_user, DataForSpecificTeacher

urlpatterns = [
    path('auth/register', RegistrationView.as_view()),
    path('auth/login', LoginView.as_view()),
    path('auth/logout', LogoutView.as_view()),
    path('verify', VerifyOTP.as_view()),
    path('password_reset/', CustomResetPasswordRequestToken.as_view(), name='create_token'),
    path('set_new_password/', SetNewPassword.as_view(), name='create_token'),

    path('add_to_favorites', AddToFavoritesView.as_view()),
    path('remove_from_favorites', RemoveFromFavoritesView.as_view()),
    path('get_all_favorites', GetAllFavoritesOfUser.as_view()),

    path('check_token_validity', CheckTokenView.as_view()),

    path('check_email/', check_user.as_view()),

    path('get_data_for_specific_user/', DataForSpecificTeacher.as_view()),

    path('me', Me.as_view()),
    path('<int:pk>', ManageUsers.as_view(), name='user details'),
    path('', ManageUsers.as_view(), name='user list'),

    path('top_ten_teacher', TopTenTeacher.as_view())
]
