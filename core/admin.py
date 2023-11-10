from django.contrib import admin


class UserTimestampMixinAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
