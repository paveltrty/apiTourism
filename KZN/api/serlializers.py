from django.db.models import fields
from rest_framework import serializers
from .models import Place
from .models import Comment


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ("Name", "Location", "Tags", "rating", "Description", "Price", "Is_Approved", "Owner")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("Description", "Post", "Owner")
