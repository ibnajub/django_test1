from asgiref.sync import sync_to_async, async_to_sync
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View

# Create your views here.
from .forms import SearchForm
from .services import search_image, save_images
from .models import Image


class SearchImageView(View):
    async def get(self, request):
        return await sync_to_async(render)(request, 'search_img/index.html', {'form': SearchForm})
        # return render(request, 'search_img/index.html', {'form': SearchForm})
    
    async def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        images = []
        if form.is_valid():
            images = await search_image(form.cleaned_data['query'], form.cleaned_data['count'])
        return await sync_to_async(render)(
            request, 'search_img/index.html', {'form': SearchForm(), 'images': images}
        )


@login_required
# @async_to_sync
# async def search_save(request):
def search_save(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        images = []
        if form.is_valid():
            # images = await save_images(request.user.id,
            images = async_to_sync(save_images)(request.user.id,
                                                form.cleaned_data['query'],
                                                form.cleaned_data['count']
                                                )
        # return await sync_to_async(render)(
        return render(
            request, 'search_img/index.html', {'form': SearchForm(), 'images': images}
        )


class ListImageView(View):
    async def get(self, request):
        # images = Image.objects.filter(user=request.user)
        images = Image.objects.filter()
        return await sync_to_async(render)(request, 'search_img/list_images.html', {'images': images})
