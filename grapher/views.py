from django.shortcuts import render

# Create your views here.
def graph_test(request):
    return render(request, 'grapher/test.html', {})
