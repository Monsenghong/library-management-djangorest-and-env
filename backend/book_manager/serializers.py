from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Book ,Author,Member,BorrowedBook
from django.contrib.auth.models import User, Group



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
   

    class Meta:
        model = Author
        fields = '__all__'

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'
    



class BorrowedBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = '__all__'

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
