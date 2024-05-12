from celery import shared_task

@shared_task
def add(x, y):
    for i in range(x,y):
        print(i)
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)
