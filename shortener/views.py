from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

def kirr_redirect_view(request,shortcode=None,*args, **kwargs):
    print(request.user)
    print(request.user.is_authenticated())
    print(args)
    print(kwargs)
    return HttpResponse("hello {sc}".format(sc=shortcode))


class KirrCBView(View):
    def get(self,request,shortcode=None,*args,**kwargs):
        print(args)
        print(kwargs)
        return HttpResponse("hello again {sc}".format(sc=shortcode))