from django.shortcuts import render, redirect
from contact.forms import ContactForm

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    return render(request, 'contact/contact.html', {'form':form})