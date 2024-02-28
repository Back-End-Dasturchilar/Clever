from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login, logout
from app.models import Customer, Cours
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from app.serializers import *
import math
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class CreateCourse(CreateAPIView):
    serializer_class = CoursApi
    queryset = Cours.objects.all()
    permission_classes = [IsAdminUser]


    def post(self, req: Request):
        author_id = req.data.get('author')
        author = Teacher.objects.get(pk=author_id)
        likes = req.data.get('likes')
        db = Cours.objects.create(
            title = req.data.get('title'),
            desc = req.data.get('desc'),
            author = author,
            img = req.data.get('img'),
            view = req.data.get('view'),
            price = req.data.get('price'),
            like_count = req.data.get('like_count'),
            total = req.data.get('total'),
            like = req.data.get('like'),
        )

        db.likes.set(likes)


        return Response({'course': 'Success !!!'})

class UpdateViewCourse(RetrieveUpdateAPIView):
    serializer_class = CoursForUsersApi
    queryset = Cours.objects.all()

    def get(self, req:Request, *args, **kwargs):
        

        el = self.get_object()

        el.view += 1
        el.save()
        
        return Response(CoursApi(Cours.objects.get(pk=el.pk)).data)
    
    def put(self, req:Request, *args, **kwargs):
        obj = self.get_object()
        el = Cours.objects.get(pk=obj.pk)

        el.like_count += 1
        el.like += float(req.data.get('like'))
        if el.like_count >= 1 and el.like > 0:
            el.total += math.trunc(float(el.like) / float(el.like_count))
        el.save()
        
        return Response(CoursApi(Cours.objects.get(pk=obj.pk)).data)
        
class ListCourse(ListAPIView):
    serializer_class = CoursApi
    queryset = Cours.objects.all()

class Register(CreateAPIView):
    serializer_class = CustomerApi
    queryset = Customer.objects.all()


    def post(self, req:Request):
        el = Customer.objects.create_user(
            username = req.data.get('username'),
            site = req.data.get('site'),
            email = req.data.get('email'),
            phone = req.data.get('phone')
        )

        
        db = Customer.objects.get(pk=el.pk)

        login(request=req, user=db)

        token = RefreshToken.for_user(db)


        return Response({'access': str(token.access_token),'refresh':str(token)})

class Login(APIView):

    def post(self, req:Request, *args, **kwargs):
        username = req.data.get('username')
        email = req.data.get('email')
        
        el = Customer.objects.all().filter(username=username, email=email).first()
        print(el)

        login(request=req, user=el)

        token = RefreshToken.for_user(el)


        return Response({'access': str(token.access_token),'refresh':str(token)})


class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, req:Request, *args, **kwargs):
        logout(request=req)
        return Response({'msg':'Success !!!'})


class CatList(ListAPIView):
    serializer_class = CatApi
    queryset = Category.objects.all()

class BlogCreate(CreateAPIView):
    serializer_class = CoursApi
    queryset = Cours.objects.all()
    # permission_classes = [IsAuthenticated]

class Bloglist(ListAPIView):
    serializer_class = CoursApi
    queryset = Cours.objects.all()

class Teachers(ListAPIView):
    serializer_class = TeacherApi
    queryset = Teacher.objects.all()

# {
#  "username":"cdsafvsag",
#  "email":"fdashbfdah@gmail.com"
# }