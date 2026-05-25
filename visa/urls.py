from django.urls import path

from .views import VisaRecordAPIView, VisaSearchView

app_name = 'visa'

urlpatterns = [
    path('', VisaSearchView.as_view(), name='visa_search'),
    path('api/visa/<str:visa_number>', VisaRecordAPIView.as_view(), name='visa_api'),
]
