from rest_framework import routers
from rental import views as rental_views

router = routers.DefaultRouter()
router.register(r'friends', rental_views.FriendViewSet)
router.register(r'belongings', rental_views.BelongingViewSet)
router.register(r'borrowings', rental_views.BorrowedViewSet)
router.register(r'emotions', rental_views.EmotionViewSet)