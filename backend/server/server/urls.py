from django.contrib import admin
from django.urls import path, include
from accounts.views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from django.http import HttpResponse   # ✅ ADD THIS

# ✅ ADD THIS FUNCTION
def home(request):
    return HttpResponse("Backend is running 🚀")

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ ROOT FIX
    path('', home),

    # JWT
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # APIs
    path('api/', include('accounts.urls')),
]