from django.shortcuts import render
from feedback_form.models import DDS_feedback

# Create your views here.
def index(request):
    return render(request, 'feedback_form/index.html')


def form_submit(request):
    if request.method == "POST":
     


        question1 = request.POST["question1"]
        question2 = request.POST["question2"]
        question3 = request.POST["question3"]
        question4 = request.POST["question4"]
        question5 = request.POST["question5"]
        question6 = request.POST["question6"]
        question7 = request.POST["question7"]
        question9 = request.POST["comment"]


        feedback_results = DDS_feedback(

            question1 = question1,
            question2 = question2,
            question3 = question3,
            question4 = question4,
            question5 = question5,
            question6 = question6,
            question7 = question7,
            question = question9,
        )


        
        feedback_results.save()
        
        

        return render(
            request, "feedback_form/feedback_con.html"
        )

