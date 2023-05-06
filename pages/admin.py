from django.contrib import admin
from .models import Topic,Category,Comment,CarouselImage
# Register your models here.


class TopicAdmin(admin.ModelAdmin):
    list_display = ('titlePrefix','title','LastUpdate','author','slug',)
    search_fields = ('title','category',)
    readonly_fields = ('slug',)
    list_filter = ('category',)


admin.site.register(Topic,TopicAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(CarouselImage)
