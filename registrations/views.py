from django.shortcuts import render


def all_list(request):
    return render(request, "registrations/all_list.html")
