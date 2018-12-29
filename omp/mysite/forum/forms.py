from django.forms import ModelForm
#from myapp.models import Article
from forum.models import Topic, Post

# Create the form class.
class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_name']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_text']
