from django.contrib import messages
from communities.models import Community  # Import the Community model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import New
from django.contrib import messages

@login_required
def create_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        community_id = request.POST.get('community')

        # Ensure the user is the owner of the selected community
        community = Community.objects.filter(id=community_id, created_by=request.user).first()
        if not community:
            messages.error(request, "You can only post news for communities you own.")
            return redirect('create_news')

        # Create the news item
        New.objects.create(title=title, description=content, image=image, community=community, author=request.user)
        return redirect('news_list')

    # Pass communities owned by the user to the template
    user_communities = Community.objects.filter(created_by=request.user)
    return render(request, 'news/create_news.html', {'communities': user_communities})




# List all news with full details
def news_list(request):
    news_items = New.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news_items': news_items})





@login_required
def delete_news(request, news_id):
    news_item = get_object_or_404(New, id=news_id)

    # Allow deletion only by the author or the community owner
    if news_item.author == request.user or news_item.community.created_by == request.user:
        news_item.delete()
        messages.success(request, "News item deleted successfully.")
    else:
        messages.error(request, "You are not authorized to delete this news item.")

    return redirect('news_list')