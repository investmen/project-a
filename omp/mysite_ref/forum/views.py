from django.http import Http404,HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Post,Topic
from .forms import PostForm,TopicForm


def index(request):
    return HttpResponse("Nexii discussion forum index.")

def harini(request):
    post_list = Post.objects.all()
    output = '</br>'.join([p.post_text for p in post_list])
    return HttpResponse(output)

def post_list_html(request, topic_id):
    post_list = Post.objects.filter(topic=topic_id)
    template = loader.get_template('forum/index.html')
    context = {
          'post_list': post_list,
          'topic_id': topic_id
    }
    return HttpResponse(template.render(context,request))
     
def topic_list(request):
    #import pdb;pdb.set_trace()
    topic_list = Topic.objects.all()
    template = loader.get_template('forum/topic_index.html')
    context = {
          'topic_list': topic_list,
    }
    return HttpResponse(template.render(context,request))

def topic_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TopicForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/forum/topic/list/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TopicForm()

    return render(request, 'forum/topic_create.html', {'form': form})
    
def post_create(request, topic_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/forum/topic/'+topic_id+'/post/list/')
    else:
        form = PostForm()
    context = {
          'topic_id': topic_id,
          'form': form
    }
    #return HttpResponse(template.render(context,request))

    return render(request,'forum/post_create.html',context)
    

def detail(request, post_id, topic_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("post does not exist")
    return render(request, 'forum/detail.html', {'post': post})

def topic_detail(request, topic_id):
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        raise Http404("topic does not exist")
    return render(request, 'forum/topic_detail.html', {'topic': topic})

