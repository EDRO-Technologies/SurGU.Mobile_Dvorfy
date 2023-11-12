from django.contrib import admin
from .models import User, Task, groups

admin.site.register(User)
admin.site.register(Task)
admin.site.register(groups)
# admin.site.register(message)
# admin.site.register(Message)


