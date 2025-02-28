from django.shortcuts import render, redirect, HttpResponse
from .forms import ApplicationForm, StrawhatForm

# Create your views here.
def my_form(request):
    form = ApplicationForm()
    
    return render(request, 'formapp/forms.html', {'form': form})


def create_strawhat(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = StrawhatForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('formapp:success')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StrawhatForm()

    return render(request, "formapp/strawhats.html", {"form": form})

def success(request):
    return HttpResponse('<h2>Form submission was successful!</h2><p>Your data has been saved to the database.</p>')


# def form_view(request):
#     form = BookingForm()
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {"form" : form}
#     return render(request, "booking.html", context)