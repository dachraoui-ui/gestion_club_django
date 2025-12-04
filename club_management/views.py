from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from club_management.forms import MemberForm


def member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    else:
        form = MemberForm()

    return render(request, 'Member.html', {'form': form})

