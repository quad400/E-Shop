import admin_thumbnails
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import (
            Images,UserProfile, Setting, Category, 
            Product, Comment,Order, Cart,FAQ,
            Size, Color, Variant,BillingAddress
                    )


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = 'title'
    list_display = ['tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count']
    list_display_links = ['indented_title']
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(qs, Product, 
                        'category', 'products_cumulative_count', cumulative=True)
        
        qs = Category.objects.add_related_count(qs, Product, 
                        'category', 'products_count', cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1
    show_change_link = True
    readonly_fields = ('image_tag',)

# @admin_thumbnails.thumbnail('image')
class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 1
    readonly_fields = ('id_tag','image_tag',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','price', 'image_tag']
    list_display_links = ['title', 'price']
    # list_filter = ['category']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImagesInline, VariantInline]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['product','user','subject', 'rate']
    list_display_link = ['product']
    list_filter = ['rate']
    readonly_fields = ('product','user','subject', 'rate','ip', 'content')

class CartAdmin(admin.ModelAdmin):
    list_display = ['product','user','quantity','get_price']
    list_display_link = ['product']
    list_filter = ['ordered']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',]
    list_filter = ['ordered']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone','city','country']
    list_filter = ['country']

class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']

class ColorAdmin(admin.ModelAdmin):
    list_display = ['name','color_tag']



admin.site.register(Setting)
admin.site.register(Images)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size)
admin.site.register(BillingAddress)
