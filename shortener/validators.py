from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
    url_validator = URLValidator()
    value_invalid = False


    """if "http://" in value:
        valid_url = value
    else:
        valid_url = "http://" + value
        print(valid_url)

    try:
        url_validator(valid_url)
    except:
        value_invalid = True

    if value_invalid:
            raise ValidationError("Invalid URL for this field")"""
    try:
         url_validator(value)
  
    except:
        raise ValidationError("Invalid URL for this field, add correct protocol e.g http,https,ftp")

    #if not "http" in value:
       # raise ValidationError("Invalid URL for this field")
    #print(new_value)
    return value

def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError("This is not valid because of no .com")
    return value
