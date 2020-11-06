from django.shortcuts import render

# Create your views here.
def home(request):
    data = ""
    return render(request, 'index.html', {'data' : data})


def dashboard(request):
    data = ""
    return render(request, 'dashboard.html', {'data': data})


def ticketDetail(request):
    data = ""
    return render(request, 'ticket_detail.html', {'data': data})