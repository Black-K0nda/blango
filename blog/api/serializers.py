from blog.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = "__all__"
    readonly = ['modified_at', 'created_at']