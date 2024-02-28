from rest_framework.serializers import ModelSerializer
from app.models import *


class CustomerApi(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username','site','phone','email']


class TeacherApi(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class CoursApi(ModelSerializer):
    author = TeacherApi
    likes = CustomerApi
    class Meta:
        model = Cours
        fields = '__all__'

class CoursForUsersApi(ModelSerializer):
    likes = CustomerApi
    class Meta:
        model = Cours
        fields = ['view', 'like', 'like_count', 'likes']

class CatApi(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BlogApi(ModelSerializer):
    category = CatApi()
    class Meta:
        model = Blog
        fields = '__all__'