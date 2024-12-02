from django.urls import path
from .views import (
    InternshipListCreateView,
    InternshipDetailView,
    UsersMeView,SignUpView,
    LoginView, LogoutView
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('internships/', InternshipListCreateView.as_view(), name='internship-list-create'),
    path('internships/<int:pk>/', InternshipDetailView.as_view(), name='internship-detail'),
    path('users/me', UsersMeView.as_view(), name='users-me'),
]