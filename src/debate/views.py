from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Debate, Comment
from .forms import NewComment
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def debate_index(request, *args, **kwargs):
    debate_pk = kwargs.get('pk')
    print(debate_pk)
    debate = Debate.objects.get(pk=debate_pk)
    comments = Comment.objects.filter(debate__pk=debate_pk)
    context = {
        'debate': debate,
        'comments': comments
    }
    return render(request, 'debate/debate.html', context)


def new_comment(request, *args, **kwargs):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        else:
            return HttpResponse('Please login first')
        # create a form instance and populate it with data from the request:
        form = NewComment(request.POST or None)
        debate_id = kwargs.get('pk')
        print('post:', request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            comment = form.cleaned_data.get('comment')
            print('username:', username, '- comment:', comment, '- PK:', debate_id)
            if comment is not None and debate_id is not None:
                try:
                    creator = request.user
                    print('creator:',creator)
                    new_comment = Comment(creator=creator, body=comment, debate_id=debate_id)
                    new_comment.save()
                except Exception as E:
                    print(str(E))
                    return HttpResponse('The Debate is not exists or the comment can not be saved.')
                # redirect to a new URL:
                return HttpResponseRedirect(reverse('debate',kwargs={'pk':debate_id}))
        else:
            return HttpResponse('Form is not valid')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewComment()

    return render(request, 'name.html', {'form': form})
