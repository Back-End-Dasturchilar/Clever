from django.urls import path
from app.views import *

urlpatterns = [
    path('course/', CreateCourse.as_view(), name='course'),
    path('detail/<int:pk>/', UpdateViewCourse.as_view(), name='detail'),
    path('courses/', ListCourse.as_view(), name='courses'),
    path('singup/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('cat/', CatList.as_view(), name='cat'),
    path('create/', BlogCreate.as_view(), name='create'),
    path('blog/', Bloglist.as_view(), name='blog'),
    path('teachers/', Teachers.as_view(), name='teacher')
]
