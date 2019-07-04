import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from socialnetwork.serializers import UserSerializer, PostSerializer
from .models import User, Post, Relationship

from rest_framework.response import Response


class UserView(APIView):

    def get(self, request):

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OneUserView(APIView):

    def get(self, request, **kwargs):
        users = User.objects.filter(user_id=kwargs['user_id'])
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)


class RelationshipView(APIView):
    def add_relationship(self, user, status):
        relationship, created = Relationship.objects.get_or_create(
            from_user=self,
            to_user=user,
            status=status)
        return relationship


class MyLoginView(APIView):
    @csrf_exempt
    def post(self, request, **kwargs):
        received_json_data = json.loads(request.body.decode("utf-8"))
        mailx = received_json_data['mail']
        password = received_json_data['password']
        user = User.objects.filter(mail=mailx).first()
        if user is not None:
            if user.mail == mailx:
                if user.password == password:
                    return JsonResponse(user.user_id, safe=False)
                else:
                    return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)


class SearchView(APIView):

    def post(self,request):

        received_json_data = json.loads(request.body.decode("utf-8"))
        var = received_json_data['string']
        users = (User.objects.filter(first_name__istartswith=var) |
                User.objects.filter(last_name__istartswith=var))
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)



class PostView(APIView):
    def get(self, request):

        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OnePostView(APIView):

    def get(self, request, **kwargs):
        posts = Post.objects.filter(user_id=kwargs['user_id'])
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)