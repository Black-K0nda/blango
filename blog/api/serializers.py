from blog.models import Post, Comment, Tag
from blango_auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email']

class TagField(serializers.SlugRelatedField):
  def to_internal_value(self, data):
    try:
      return self.get_queryset().get_or_create(Value=data.lower())[0]
    except (TypeError, ValueError):
      self.fail(f"Tag value {data} is invalid")


class CommentSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(required=False)
  creator = UserSerializer(read_only=True)

  class Meta:
    model = Comment
    fields = ['id', 'creator', 'content', 'modified_at', 'created_at']
    read_only = ['modified_at', 'created_at']


class PostSerializer(serializers.ModelSerializer):
  tags = serializers.SlugRelatedField(
    slug_field="value", many=True,
    queryset=Tag.objects.all()
  )

  author = serializers.HyperlinkedRelatedField(
    queryset=User.objects.all(),
    view_name='api_user_detail',
    lookup_field='email'
  )

  class Meta:
    model = Post
    fields = "__all__"
    readonly = ['modified_at', 'created_at']