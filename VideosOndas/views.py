from django.shortcuts import render
from .models import VideosOndas
# Create your views here.

def galeriaVideos(request):
	videos = VideosOndas.objects.all()

	return render(request, 'ondas_videos.html', {'videos':videos})