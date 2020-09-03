from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.db.models import F
from .models import URL
from .forms import UrlField
from .encodeURL import encode
from django.urls import reverse
# Create your views here.


class Shortener(View):

    def get(self, request):

        template_name = 'main/home.html'
        form = UrlField()
        context = {'form': form}
        context['shorten_url'] = request.GET.get('shorten_url')
        return render(request, template_name, context)

    def post(self, request):
        template_name = 'main/home.html'
        model = URL
        form = UrlField(request.POST)
        context = {}
        if form.is_valid():
            new_url = form.save(commit=False)
            last_id = model.objects.latest('id').id
            short_url = encode(last_id+1)
            new_url.short_url = short_url
            new_url.save()
            context['shorten_url'] = 'http://127.0.0.1:8000/'+short_url
        else:
            context['error'] = 'Seems like thats not a link'
        return JsonResponse(context, status=200)


class Redirect_from_url(View):
    def get(self, request, short_url):
        model = URL
        full_url = model.objects.select_related().get(short_url=short_url)
        full_url.used_count = full_url.used_count + 1
        full_url.save()
        return redirect(full_url.full_url)


class Link_list(View):
    def get(self, request):
        model = URL
        template_name = 'main/links.html'
        links = model.objects.all()
        context = {'links': links[1::]}
        return render(request, template_name, context)
