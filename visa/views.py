from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views import View

from .models import VisaRecord


class VisaSearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        visa_number = self.request.GET.get('visa_number', '').strip()
        context['search_query'] = visa_number
        context['record'] = None

        if visa_number:
            context['record'] = VisaRecord.objects.filter(visa_number__iexact=visa_number).first()
        return context


class VisaRecordAPIView(View):
    def get(self, request, visa_number):
        record = get_object_or_404(VisaRecord, visa_number__iexact=visa_number)
        data = {
            'visa_number': record.visa_number,
            'surname': record.surname,
            'first_name': record.first_name,
            'father_name': record.father_name,
            'date_of_birth': record.date_of_birth.isoformat(),
            'citizenship': record.citizenship,
            'passport_number': record.passport_number,
            'passport_issue_date': record.passport_issue_date.isoformat(),
            'passport_expiry_date': record.passport_expiry_date.isoformat(),
            'visa_status': record.visa_status,
            'visa_validity': record.visa_validity,
            'visa_type': record.visa_type,
            'visit_purpose': record.visit_purpose,
            'approval_date': record.approval_date.isoformat() if record.approval_date else None,
            'issue_date': record.issue_date.isoformat() if record.issue_date else None,
            'duration_of_stay': record.duration_of_stay,
            'number_of_entries': record.number_of_entries,
            'reference_number': record.reference_number,
            'photo_url': request.build_absolute_uri(record.photo.url) if record.photo else None,
        }
        return JsonResponse(data)
