from django_filters import rest_framework as filters
from rest_framework import serializers, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Place, Comment
from .serlializers import PlaceSerializer, CommentSerializer


class PlaceFilter(filters.FilterSet):

    class Meta:
        model = Place
        fields = {
            'Name': ['contains'],
            'Tags': ['contains'],
        }


class PlaceList(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    name = 'place-list'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlaceFilter

# Create your views here.
@api_view(['POST'])
def add_post(request):
    post = PlaceSerializer(data=request.data)

    # validating for already existing data
    if Place.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if post.is_valid():
        post.save()
        return Response(post.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_posts(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Place.objects.filter(**request.query_params.dict())
    else:
        items = Place.objects.all()

    # if there is something in items else raise error
    if items:
        serializer = PlaceSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def update_post(request, pk):
    post = Place.objects.get(pk=pk)
    data = PlaceSerializer(instance=post, data=request.data)
    permission_classes = (IsAuthenticated, )
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_comments(request, pk):
    post = Place.objects.get(pk=pk)
    comments = post.comment_set.all()

    if comments:
        serializer = PlaceSerializer(comments, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_comment(request):
    comment = CommentSerializer(data=request.data)

    # validating for already existing data
    if Comment.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if comment.is_valid():
        comment.save()
        return Response(comment.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_comment(request, pk):
    post = Place.objects.get(pk=pk)
    data = PlaceSerializer(instance=post, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

