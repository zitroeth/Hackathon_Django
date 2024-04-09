from requests import Response
from rest_framework import viewsets
from rest_framework import status
from . import models
from . import serializers
from .emotion import getEmotion
from .serializers import EmotionSerializer

class FriendViewSet(viewsets.ModelViewSet):
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer
class BelongingViewSet(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer
class BorrowedViewSet(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer
class EmotionViewSet(viewsets.ModelViewSet):
    queryset = models.Emotion.objects.all()
    serializer_class = serializers.EmotionSerializer

    # def get(self, request):
    #     thoughts = request.data.get('thoughts', '')
    #     print(thoughts)
    #     emotions = getEmotion(thoughts)
    #     return Response(emotions)
    
    def post(self, request):
        thoughts = request.data.get('thoughts', '')
        emotions = getEmotion(thoughts)

        analysis_result = models.Emotion.objects.create(
            thoughts=thoughts,
            emotions=emotions
        )

        serializer = EmotionSerializer(analysis_result)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)