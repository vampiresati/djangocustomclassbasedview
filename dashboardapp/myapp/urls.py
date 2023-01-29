from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path("login/", views.MyLoginView.as_view(), name="login"),
    path("profile/",TemplateView.as_view(template_name='myapp/profile.html'),name='profile'),
    path("logout/", views.MyLogoutView.as_view(), name="logout"),
    path("passwordchange/", views.MyPasswordChangeView.as_view(), name="passwordchange"),
    path("passwordchangedone/", views.PasswordChangeDoneView.as_view(), name="passwordchangedone"),
    # path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    # path("password_reset/done/",views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    # path("reset/<uidb64>/<token>/",views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    # path("reset/done/",views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]
