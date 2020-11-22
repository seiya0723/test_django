from django.shortcuts import render

# Create your views here.
from django.views import View

class IndexView(View):

    def get(self, request, *args, **kwargs):

        if "comment" in request.GET:
            data    = request.GET["comment"]
            print(data)

        return render(request,"index.html")

    def post(self, request, *args, **kwargs):

        data    = request.POST["comment"]

        context = { "data":data }
            
        return render(request,"index.html",context)
        #return render(request,"index.html")

index   = IndexView.as_view()
