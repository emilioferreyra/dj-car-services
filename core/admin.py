from django.contrib import admin


class UserTimestampMixinAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

    def save_formset(self, request, obj, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if hasattr(instance, 'created_by') and instance.created_by is not None:
                # Verificar si existe created_by antes de actualizar updated_by
                instance.updated_by = request.user
            instance.created_by = request.user
            instance.save()
        formset.save()
