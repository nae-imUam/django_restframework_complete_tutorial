from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICE, STYLE_CHOICES
"""
class SnippetSerializer(serializers.ModelSerializer):
    
    '''id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICE, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validate_data):
        return Snippet.objects.create(**validate_data)
    
    def update(self, instance, validate_data):
        instance.title = validate_data.get('title', instance.title)
        instance.code = validate_data.get('code', instance.code)
        instance.linenos = validate_data.get('linesnos', instance.linenos)
        instance.language = validate_data.get('language', instance.language)
        instance.style = validate_data.get('style', instance.style)
        instance.save()
        return instance'''
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']

        """

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')


    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']


from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']

        