from django.shortcuts import redirect, render
import requests
base_url='http://ec2-34-208-165-8.us-west-2.compute.amazonaws.com/'


def activate(request, uid, token):
    endpoint = base_url + "auth/users/activation/"
    r = requests.post(endpoint, json={"uid":uid,"token":token})
    return redirect('userlist')

def password_reset_confirm(request, uid, token):
    endpoint = base_url + "auth/users/reset_password_confirm/"
    r = requests.post(endpoint, json={"uid":uid,"token":token})
    return redirect('userlist')