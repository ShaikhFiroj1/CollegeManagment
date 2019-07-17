from django.urls import path, include
from Student.views import IndexView , StudentCreateView, StudentUpdateView, StudentDeleteView


urlpatterns = [
    
    path('', IndexView.as_view(), name='home'),
    path('addnew/', StudentCreateView.as_view(), name='newstudent'),
    path('<int:pk>/update/', StudentUpdateView.as_view(), name='updatestudent'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='deletestudent'),
]
