from django.contrib import admin
from .models import Members
from django.contrib.auth.models import User, Group
# from
# Register your models here.

@admin.register(Members)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("username", "disabled")
    list_filter = ("disabled", )
    search_fields = ("username__startswith", )
    # exclude = ('member_id',)
    
    def save_model(self, request, obj, form, change):
        # obj.added_by = request.user
        obj.challenge_question = "test question"
        super().save_model(request, obj, form, change)


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.site_header = "ClubTravels Admin"