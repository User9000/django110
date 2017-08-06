
import random
import string 
#from shortener.models import KirrURL


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    #new_code  = ''
    #for _ in range(size):
    #new_code += random.choice(chars)
    #return new_code
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    #copy instance class and send it to KirrURL variable
    Klass = instance.__class__
    #query set
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code


