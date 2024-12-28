from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Community, CommunityMember

# List all communities
def community_list(request):
    communities = Community.objects.all().order_by('-created_at')
    return render(request, 'communities/community_list.html', {'communities': communities})

# View a specific community
def community_detail(request, community_id):
    community = get_object_or_404(Community, id=community_id)
    members = CommunityMember.objects.filter(community=community)
    is_member = request.user.is_authenticated and CommunityMember.objects.filter(user=request.user, community=community).exists()
    return render(request, 'communities/community_detail.html', {'community': community, 'members': members, 'is_member': is_member})

# Create a new community
@login_required
def create_community(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        thumbnail = request.FILES.get('thumbnail')  # Get the uploaded thumbnail
        Community.objects.create(
            name=name,
            description=description,
            thumbnail=thumbnail,
            created_by=request.user
        )
        return redirect('community_list')
    return render(request, 'communities/create_community.html')


# Join a community
@login_required
def join_community(request, community_id):
    community = get_object_or_404(Community, id=community_id)
    CommunityMember.objects.get_or_create(user=request.user, community=community)
    return redirect('community_detail', community_id=community.id)

# Leave a community
@login_required
def leave_community(request, community_id):
    community = get_object_or_404(Community, id=community_id)
    membership = CommunityMember.objects.filter(user=request.user, community=community)
    if membership.exists():
        membership.delete()
    return redirect('community_detail', community_id=community.id)
