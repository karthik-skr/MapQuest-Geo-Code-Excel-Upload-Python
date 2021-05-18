from django.shortcuts import render
from django.http import HttpResponse
from .app_utils import file_processor as fp
def index(request):
    if request.method == "GET":
        return render(request, "app/index.html", {})
    else:
        input_file = request.FILES["input_file"]
        resp_obj = fp.process_file(input_file)
        if resp_obj["message"] == "success":
            response = HttpResponse(content=resp_obj["data"], content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename={0}'.format(resp_obj["file_name"])
            return response
        else:
            return  HttpResponse("Sorry")