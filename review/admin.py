from django.contrib import admin
from review.models import ReviewModel

class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Phone_no','Rating','Comment')

admin.site.register(ReviewModel, ReviewModelAdmin)