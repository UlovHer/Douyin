import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from douyin import settings


def home(request):
    return render(request, 'home.html')


# 跨域请求
@csrf_exempt
def download(request):
    video_url_web = request.GET.get('video_url_web')
    video_name = request.GET.get('video_name')
    video_local_path = os.path.join(settings.LOCALE_DIR, video_name).replace('\\', '/')
    # print(video_local_path)
    if not video_url_web:
        return render(request, 'home.html', locals())
    return render(request, 'download.html', locals())
