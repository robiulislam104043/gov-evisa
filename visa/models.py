from django.db import models


class VisaRecord(models.Model):
    STATUS_VALID = 'Valid'
    STATUS_INVALID = 'Invalid'
    VISA_STATUS_CHOICES = [
        (STATUS_VALID, 'Valid'),
        (STATUS_INVALID, 'Invalid'),
    ]

    visa_number = models.CharField(max_length=64, unique=True)
    surname = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    father_name = models.CharField(max_length=128, blank=True)
    date_of_birth = models.DateField()
    citizenship = models.CharField(max_length=128)
    passport_number = models.CharField(max_length=64)
    passport_issue_date = models.DateField()
    passport_expiry_date = models.DateField()
    visa_status = models.CharField(
        max_length=16,
        choices=VISA_STATUS_CHOICES,
        default=STATUS_INVALID,
    )
    visa_validity = models.CharField(max_length=64, blank=True)
    visa_type = models.CharField(max_length=64)
    visit_purpose = models.CharField(max_length=128)
    approval_date = models.DateField(blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    duration_of_stay = models.PositiveIntegerField(blank=True, null=True, help_text='Duration in days')
    number_of_entries = models.PositiveIntegerField(default=1)
    reference_number = models.CharField(max_length=128, blank=True)
    photo = models.ImageField(upload_to='visa_photos/', blank=True, null=True)

    class Meta:
        ordering = ['visa_number']
        verbose_name = 'Visa Record'
        verbose_name_plural = 'Visa Records'

    def __str__(self):
        return f'{self.visa_number} — {self.surname}, {self.first_name}'
