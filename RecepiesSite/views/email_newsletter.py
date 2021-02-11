from django.conf import settings
from RecepiesSite.forms.email_sub_form import EmailSignupForm
from RecepiesSite.Models.email_sub import Signup
import requests
import json
from django.contrib import messages
from django.http import HttpResponseRedirect

MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'

members_endpoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'


def subscribe(email):
    data = {
        'email_address': email,
        'status': 'subscribed'
    }
    r = requests.post(
        members_endpoint,
        auth=('', MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )
    return r.status_code, r.json()


def email_list_signup(request):
    e_form = EmailSignupForm(request.POST or None)
    if request.method == "POST":
        if e_form.is_valid():
            email_signup_qs = Signup.objects.filter(email=e_form.instance.email)
            if email_signup_qs.exists():
                messages.warning(request, 'You are already subscribed!')
            else:
                subscribe(e_form.instance.email)
                e_form.save()
                messages.success(request, 'You are subscribed now.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


