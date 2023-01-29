from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.hello,name='hello'),
    path("login/", auth_views.LoginView.as_view(template_name="myapp/login.html"), name="login"),
    path("profile/",TemplateView.as_view(template_name='myapp/profile.html'),name='profile'),
    path("logout/", auth_views.LogoutView.as_view(template_name="myapp/logout.html"), name="logout"),
    path("passwordchange/", auth_views.PasswordChangeView.as_view(template_name="myapp/password_change.html",success_url='/myapp/passwordchangedone/'), name="passwordchange"),
    path("passwordchangedone/",auth_views.PasswordChangeDoneView.as_view(template_name="myapp/passwordchangedone.html"),name="passwordchangedone"),
    # path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    # path("password_reset/done/",views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    # path("reset/<uidb64>/<token>/",views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    # path("reset/done/",views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]
