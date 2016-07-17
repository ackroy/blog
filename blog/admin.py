from django.contrib import admin
from .models import Article, Tag, Classification



# class ArticleAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': []}),
#         ('Date information', {'fields': [], })
#     ]

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Classification)
# admin.site.register(Author)



