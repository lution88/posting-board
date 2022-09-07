from django.core.exceptions import ValidationError


def validate_no_number(value):
    ''' 비밀번호에 숫자가 포함되지 않으면 Validation Error를 일으킨다. '''

    if not any(chr.isdigit() for chr in value):
        raise ValidationError("비밀번호에 숫자가 1개 이상 포함되어야 합니다.")


def validate_gte_6chars(value):
    ''' 비밀번호 길이가 min_length 미만이면 Validation Error를 일으킨다.'''

    min_length = 6

    if len(value) < min_length:
        raise ValidationError(f"비밀번호는 {min_length}자 이상이어야 합니다.")
