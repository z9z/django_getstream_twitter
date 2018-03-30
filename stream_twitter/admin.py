from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from stream_twitter.models import Tweet, UserProfile

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton


class TweetInline(admin.TabularInline):
    model = Tweet
    extra = 0
    fields = ('user', 'text',)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, TweetInline)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
