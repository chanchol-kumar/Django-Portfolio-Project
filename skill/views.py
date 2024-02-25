from django.shortcuts import render,redirect
from skill.models import SkillModel
from skill.forms import SkillForm

def add_skill(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skill')
    else:
        form = SkillForm()
    return render(request, 'skill/add_skill.html', {'form':form})

def skill(request):
    skill = SkillModel.objects.all()
    return render(request, 'skill/skill.html', {'skill': skill})
