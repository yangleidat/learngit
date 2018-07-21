from django.shortcuts import render
from .models import DataTable

# Create your views here.

def getfrom(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        mobile = request.POST.get('mobile', '')
        service = request.POST.get('service', '')
        waiting_time = request.POST.get('waiting_time', '')
        overall_satisfaction = request.POST.get('overall_satisfaction', '')
        attitude = request.POST.get('attitude', '')
        cycle = request.POST.get('cycle', '')
        eat = request.POST.get('eat', '')
        proposal = request.POST.get('proposal', '')
        all_data = DataTable()
        all_data.name = name
        all_data.mobile = mobile
        all_data.service = service
        all_data.waiting_time = waiting_time
        all_data.overall_satisfaction = overall_satisfaction
        all_data.attitude = attitude
        all_data.cycle = cycle
        all_data.eat = eat
        all_data.proposal = proposal
        all_data.save()

    return render(request, 'khpj.html')


