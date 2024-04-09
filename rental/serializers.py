from rest_framework import serializers
from . import models
from .emotion import getEmotion

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Friend
        fields = ('id', 'name')
class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Belonging
        fields = ('id', 'name')
class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Borrowed
        fields = ('id', 'what', 'to_who', 'when', 'returned')
class EmotionSerializer(serializers.ModelSerializer):
    emotions = serializers.SerializerMethodField(read_only=True, required=False)
    class Meta:
        model = models.Emotion
        fields = ('id', 'thoughts', 'emotions')
    def get_emotions(self, obj):
        thoughts = obj.thoughts
        emotions = getEmotion(thoughts)
        return emotions