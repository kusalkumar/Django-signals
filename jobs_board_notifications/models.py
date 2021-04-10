from django.db import models

# Create your models here.
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from jobs_board_main.signals import new_subscriber
from jobs_board_main.models import Job, Subscriber, Subscription

#def handle_new_subscription(sender, **kwargs):
#@receiver(new_subscriber, sender=Subscription)
@receiver(new_subscriber)
def handle_new_subscription(**kwargs):
    print("---------------")
    subscriber = kwargs['subscriber']
    job = kwargs['job']

    message = """User {} has just subscribed to the Job {}.
    """.format(subscriber.email, job.title)

    print(message)

@receiver(new_subscriber)
def handle_new_subscriptions(sender, **kwargs):
    subscriber = kwargs['subscriber']
    job = kwargs['job']

    message = """duplicate: User {} has just subscribed to the Job {}.
    """.format(subscriber.email, job.title)
    print(message)


@receiver(pre_delete, sender=Job)
def handle_deleted_job_posting(**kwargs):
    job = kwargs['instance']

    # Find the subscribers list
    subscribers = Subscription.objects.filter(job=job)

    for subscriber in subscribers:
        message = """Dear {}, the job posting {} by {} has been taken down.
        """.format(subscriber.email, job.title, job.company)

        print(message)
