'''
Created on 2015. 10. 31.

@author: ahn
'''
from django.shortcuts import render_to_response

def main(request):
     return render_to_response('index.html')
 
def map(request):
    return render_to_response('map.html')

def mission_info(request):
    return render_to_response('mission_info.html')