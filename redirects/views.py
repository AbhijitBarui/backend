from django.shortcuts import redirect, render
import requests
base_url='http://127.0.0.1:8000/'


def activate(request, uid, token):
    endpoint = base_url + "auth/users/activation/"
    r = requests.post(endpoint, json={"uid":uid,"token":token})
    return redirect('userlist')

def password_reset_confirm(request, uid, token):
    endpoint = base_url + "auth/users/reset_password_confirm/"
    r = requests.post(endpoint, json={"uid":uid,"token":token})
    return redirect('userlist')