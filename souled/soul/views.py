from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from .forms import MessageForm


# Create your views here.


def products(request):
    return render(request, 'soul/products.html')


def user(request):
    return render(request, 'soul/user.html')

def home(request):
    return render(request, 'soul/index.html')




def message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})  # Return success response in JSON format
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
    return render(request, 'your_template.html', {'form': form})



