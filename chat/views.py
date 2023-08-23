from django.shortcuts import render, get_object_or_404,reverse
from django.contrib.auth import get_user_model
from chat.models import Message
from django.db.models import   Q
from chat.forms import MessageForm
from django.http import HttpResponseRedirect
from chat.models import Message
from django.contrib import messages



User = get_user_model()


def message(request):
    users = User.objects.exclude(username=request.user.username)
    context = {"users":users, "user_list": True}
    return render(request, "chat.html", context)



def user_chat(request, username):
    user = get_object_or_404(User, username=username)
    users = User.objects.all()
    messages = Message.objects.filter(
        Q(from_user=user, to_user=request.user) | Q(from_user=request.user, to_user=request.user)
    )
    form = MessageForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.from_user = request.user
        obj.to_user = user
        obj.save()
        return HttpResponseRedirect(reverse("chat:user_chat", args=(username,)))
    context = {"users":users, "messages":messages, "form":form}
    return render(request, 'chat.html', context)



# def delete_post(request):
#     post_id = request.POST.get("post_id")
#     print(f"Post ID: {post_id}")
#     post = get_object_or_404(Post, id=post_id, user=request.user)
#     post.delete()
#     messages.add_message(request, messages.INFO,"Your delete success")
#     return HttpResponseRedirect(reverse("post:home"))

# ChatMessage.objects.filter(user=request.user).delete()

def delete_message(request):
    # chat_id = request.POST.filter("chat_id")
    # chat = get_object_or_404(Message, id=chat_id, user=request.user)
    # chat.delete()
    message_id = request.POST.get("message_id")
    print(f"Message ID: {message_id}")
  
    chat = get_object_or_404(Message, id=message_id, to_user=request.user )
    chat.delete()
    messages.add_message(request, messages.INFO,"Your delete success")
    return HttpResponseRedirect(reverse("post:home"))

