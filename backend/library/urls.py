from django.urls import path, include

from rest_framework import routers, serializers, viewsets
from book_manager.views import BookViewSet,UserViewSet,MemberViewSet,AuthorViewSet,BorrowedBookViewSet



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)
router.register(r'borrow', BorrowedBookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('', include('account.urls')),
    path('api/', include('authentication.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]