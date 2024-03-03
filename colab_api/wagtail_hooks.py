from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet
from .models import Profile, Item

class ProfileViewSet(SnippetViewSet):
    model = Profile
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")

class ItemViewSet(SnippetViewSet):
    model = Item
    list_display = ("profile", "title", "type")
    search_fields = ("profile", "title", "type")

class AuthenticationViewSetGroup(SnippetViewSetGroup):
    items = (ProfileViewSet, ItemViewSet)
    menu_icon = "folder-inverse"
    menu_label = "Profiles"
    menu_name = "Profiles"


# When using a SnippetViewSetGroup class to group several SnippetViewSet classes together,
# only register the SnippetViewSetGroup class. You do not need to register each snippet
# model or viewset separately.
register_snippet(AuthenticationViewSetGroup)