from django.shortcuts import redirect, render


# def chat_box(request):
#     return render(request, "chat/chat.html")


def chat_box(request):
    user = request.user
    print(11111111)
    print(user)
    if not user.is_authenticated:
        return redirect('/accounts/login')
    return render(request, "chat/chat.html", {'username': user})
