from django.shortcuts import render

# Create your views here.

def chat(request):
    rid = request.GET.get('rid')
    return render(request, 'chat.html',{'rid':rid})