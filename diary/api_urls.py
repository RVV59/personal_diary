from rest_framework.routers import DefaultRouter
from .views import EntryViewSet


# Создаем роутер и регистрируем наш ViewSet
router = DefaultRouter()
router.register(r'entries', EntryViewSet, basename='entry')

# URL-шаблоны для API определяются роутером автоматически.
urlpatterns = router.urls
