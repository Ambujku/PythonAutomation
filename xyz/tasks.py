from celery import task
import sched, time
import smtplib

s = sched.scheduler(time.time, time.sleep)
@task()
def print_time(): print "From print_time", time.time()

def email_send():
    server=smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    server.login('ambujeshkumar05@gmail.com', 'A*********48')

    server.sendmail('ambujeshkumar05@gmail.com', 'paultonom@gmail.com', 'content')

def send_email():   
    print time.time()
    s.enter(1, 1, email_send, ())
    s.enter(100000000, 1, email_send, ())
    s.run()
    print time.time()
send_email()
