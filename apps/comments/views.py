from django.shortcuts import redirect

from apps.news.models import News
from apps.comments.models import Comment


def create_comment(request, pk):
    if request.method == 'POST':
        news = News.objects.get(id=pk)
        text = request.POST.get('text')
        print(text)

        com = Comment.objects.create(
            user=request.user,
            news=news,
            text=text,
        )
        com.save()

        return redirect('news_detail', news.id)
    return redirect('/')
