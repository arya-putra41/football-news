from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406406300',
        'name': 'Arya Putra Parikesit',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)

# Create your views here.
