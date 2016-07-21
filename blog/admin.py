from django.contrib import admin
from .models import Blog, Category, Comment


# class ArticleAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': []}),
#         ('Date information', {'fields': [], })
#     ]

admin.site.register(Blog)
# admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
# admin.site.register(Author)



