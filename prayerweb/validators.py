from django.core.exceptions import ValidationError

def validate_sunday(date):
    if date.isoweekday() != 7:
        raise ValidationError('%s is not a Sunday' % date)
