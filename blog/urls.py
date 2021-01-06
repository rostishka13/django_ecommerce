from django.urls import path
from .views import HomeView, ArticleDetailView, CreatePostView, DeletePostView,UpdatePostView

urlpatterns = [
	path('', HomeView.as_view(), name = 'home_blog'),
	path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article'),
	path('add_post/', CreatePostView.as_view(), name = 'add_post'),
    path('article/edit/<int:pk>/',UpdatePostView.as_view(), name = 'edit_post'),
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name = 'delete_post'),

]
 	# path('add_category/', CreateCategory.as_view(), name = 'add_category'),
  #   path('article/edit/<int:pk>', UpdatePostView.as_view(), name = 'update_post'),
  #   path('article/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),