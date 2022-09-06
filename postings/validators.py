from django.core.exceptions import ValidationError


def validate_no_number(value):
    if not any(chr.isdigit() for chr in value):
        raise ValidationError("숫자가 없습니다.")


def validate_gte_6chars(value):
    if len(value) < 6:
        raise ValidationError("비밀번호는 6자 이상이어야 합니다.")
