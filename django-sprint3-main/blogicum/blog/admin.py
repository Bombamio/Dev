from django.contrib import admin


from .models import Category, Location, User, Post


admin.site.empty_value_display = 'Не задано'


class PostInLine(admin.StackedInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (PostInLine,)
    list_display = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'location',
        'category',
        'author',
        'is_published',
        'pub_date',
    )
    list_editable = (
        'location',
        'category',
        'is_published',
    )
    search_fields = ('title',)
    list_filter = ('category', 'location', 'is_published',)
    list_display_links = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location)
