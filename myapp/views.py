from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import Band

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django!</h1>
        <p>Mes groupes préférés :</p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>                
""")