from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# jobs_board_main/views.py

from .models import Job, Subscriber, Subscription
from .signals import new_subscriber
from django.http import JsonResponse

def get_jobs(request):
    # get all jobs from the DB
    jobs = Job.objects.all()
    jobs_data = {}
    jobs_list = []
    for job in jobs:
        job_data = {}
        job_data["company"] = job.company
        job_data["email"] = job.company_email
        job_data["title"] = job.title
        job_data["status"] = job.status
        jobs_list.append(job_data)
    jobs_data["jobs_list"] = jobs_list
    #return JsonResponse(jobs_data, status=200)

    return render(request, 'jobs.html', {'jobs': jobs})

def get_job(request, id):
    job = Job.objects.get(pk=id)
    return render(request, 'job.html', {'job': job})

def subscribe(request, id):
    job = Job.objects.get(pk=id)
    print("^^^^^^^^^^")
    print(request.POST['email'])
    sub = Subscriber(email=request.POST['email'])
    print("-----")
    sub.save()
    print("%%%%%%%%")

    subscription = Subscription(user=sub, job=job, email=sub.email)
    subscription.save()
    print("--invoking--")
    new_subscriber.send(sender=subscription, job=job, subscriber=sub)
    print("--invoked--")

    payload = {
      'job': job,
      'email': request.POST['email']
    }
    return render(request, 'subscribed.html', {'payload': payload})


def delete_job(request, id):
    Job.objects.filter(pk=id).delete()
    return HttpResponse(status=204)

