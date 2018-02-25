from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/contact.html', {
        'content': [
            'If you want to contact me, please leave an email to me. mauryanarendra09@gmail.com'
            ]
    })
