from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from core.views import RegistrationForm, CarListView, CarView, OrderCarView, UserProfileView, \
    ProfileView, IndexRedirectView, CarListPageView, CarCreateView
from dz import settings

login_forbidden = user_passes_test(lambda u: u.is_anonymous, '/cars/', redirect_field_name=None)

urlpatterns = [
    path('', IndexRedirectView.as_view()),
    path('admin/', admin.site.urls),
    path('cars/', CarListView.as_view(), name='home'),
    path('cars/<int:pk>/', CarView.as_view(), name='car_detail'),
    path('cars/<int:pk>/order/', OrderCarView.as_view(), name='car_order'),
    path('cars/page/', CarListPageView.as_view(), name='car_page'),
    path('car/create/', CarCreateView.as_view(), name='car_create'),
    path('profile/', UserProfileView.as_view(), name='update_profile'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('login/', login_forbidden(LoginView.as_view()), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationForm.as_view(), name='signup')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
