from rest_framework.response import Response
from netflix.models import movie
from .serializers import MovieSerializer,UserSerializer
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes

@api_view(["GET",])
def index(request):
    movies = movie.objects.all()
    serializer = MovieSerializer(instance=movies,many=True)
    return Response(data= serializer.data,status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create(request):
    movies = movie.objects.all()
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data= {
            "success": True,
            "message": "Movie has been created successfully"
        },status=status.HTTP_201_CREATED)
         
    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


class movieList(generics.ListAPIView):
    queryset = movie.objects.all()
    serializer_class = MovieSerializer


class createMovie(generics.CreateAPIView):
    queryset = movie.objects.all()
    serializer_class = MovieSerializer


class updateMovie(generics.UpdateAPIView):
    queryset = movie.objects.all()
    serializer_class = MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    model = movie
    queryset = movie.objects.all()
    serializer_class = MovieSerializer




# class movieRUD (generics.RetriveUpdateDestroyAPIView):


@api_view(["POST"])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            return Response(data={
                "success": False,
                "errors": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={
            "success": True,
            "message": "User has been created successfully"
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)