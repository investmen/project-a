from django.contrib import admin

# Register your models here.
from .models import Post

#admin.site.register(Post)
#admin.site.register(Comment)
#admin.site.register(Reply)
"""
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['post_text']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [CommentInline]

admin.site.register(Post,PostAdmin)
"""
