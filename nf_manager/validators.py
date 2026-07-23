from django.core.exceptions import ValidationError
from brutils import is_valid_cnpj,remove_symbols_cnpj, is_valid_cep, remove_symbols_cep,  is_valid_phone, remove_symbols_phone, is_valid_email

def _validate_cnpj(value):
    if not is_valid_cnpj(remove_symbols_cnpj(value)):
        raise ValidationError("%(value)s não é um CNPJ válido.", params={"value": value})

def _validate_cep(value):
    if value and not is_valid_cep(remove_symbols_cep(value)):
        raise ValidationError("%(value)s não é um CEP válido.", params={"value": value})

def _validate_phone(value):
    if value and not is_valid_phone(remove_symbols_phone(value)):
        raise ValidationError("%(value)s não é um telefone válido.", params={"value": value})

def _validate_email(value):
    if value and not is_valid_email(value):
        raise ValidationError("%(value)s não é um email válido.", params={"value": value})

def _validate_op(value):
    if not value.isdigit() or len(value) != 4:
        raise ValidationError("%(value)s não é uma OP válida. A OP deve conter 4 dígitos.", params={"value": value})

def _validate_numero_end(value):
    if not value.isdigit():
        raise ValidationError("%(value)s não é um número válido. O número deve conter apenas dígitos.", params={"value": value})