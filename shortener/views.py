from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import KirrURL

# Create your views here.

class HomeView(View):
    def get(self,request, *args,**kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title":"Submit Url",
            "form":the_form,


        }
        return render(request,"shortener/home.html", context) #
    
    def post(self, request, *args, **kwargs):
       # print(request.POST)
       # print(request.POST.get('url'))
        form = SubmitUrlForm(request.POST)
        context ={
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            print(form.cleaned_data.get('url'))
            new_url = form.cleaned_data.get('url')
            obj,created = KirrURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"

        return render(request, template,context)




def test_view(request):
     return HttpResponse("some stuff")

def kirr_redirect_view(request,shortcode=None,*args, **kwargs):
    #print(request.user)
    #print(request.user.is_authenticated())
    #print(args)
    #print(kwargs)
    #obj = KirrURL.objects.get(shortcode=shortcode)
    print(request.method)
    obj = get_object_or_404(KirrURL,shortcode=shortcode)
    
    #obj_url = obj.url
    ''' try:
        obj = KirrURL.objects.get(shortcode=shortcode)
    except:
        obj = KirrURL.objects.all().first() '''
    ''' obj_url = None
    qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    if qs.exists() and qs.count() == 1:
        obj = qs.first()
        obj_url = obj.url '''
    return HttpResponseRedirect(obj.url)
    #return HttpResponse("hello {sc}".format(sc=obj.url))


class KirrCBView(View):
    def get(self,request,shortcode=None,*args,**kwargs):
        obj = get_object_or_404(KirrURL,shortcode=shortcode)
        print(args)
        print(kwargs)
        #return HttpResponse("hello again {sc}".format(sc=shortcode))
        return HttpResponseRedirect(obj.url)