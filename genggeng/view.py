from django.shortcuts import render


def hello_word(request):
    return render(request, 'base.html')
def main(request):
    return render(request, 'main.html')