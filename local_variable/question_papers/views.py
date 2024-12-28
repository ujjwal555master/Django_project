from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import QuestionPaper

# List all question papers
def paper_list(request):
    papers = QuestionPaper.objects.all().order_by('-uploaded_at')
    return render(request, 'question_papers/paper_list.html', {'papers': papers})

# View a single question paper
def paper_detail(request, paper_id):
    paper = get_object_or_404(QuestionPaper, id=paper_id)
    return render(request, 'question_papers/paper_detail.html', {'paper': paper})

# Upload a new question paper
@login_required
def upload_paper(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subject = request.POST.get('subject')
        exam_type = request.POST.get('exam_type')
        file = request.FILES.get('file')
        QuestionPaper.objects.create(
            title=title, 
            subject=subject, 
            exam_type=exam_type, 
            uploaded_by=request.user, 
            file=file
        )
        return redirect('paper_list')
    return render(request, 'question_papers/upload_paper.html')

# Delete a question paper
@login_required
def delete_paper(request, paper_id):
    paper = get_object_or_404(QuestionPaper, id=paper_id)
    if request.user == paper.uploaded_by:
        paper.delete()
    return redirect('paper_list')

