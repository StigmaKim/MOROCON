'''
Created on 2015. 10. 31.
@author: ahn
'''
from django.shortcuts import render_to_response
from Robocon.models import Map, Robot
from google.appengine.ext import db
import cgi
from django.http.response import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from Robocon.MapManager import MapManager
import logging
from Robocon.RobotManager import RobotManager
from Robocon.MissionManager import MissionManager

try:
    import json
except ImportError:
    import simplejson as json

RobotManagerIns = RobotManager()
MapManagerIns = MapManager()
MissionManagerIns = MissionManager() 
    
def main(request):
    return render_to_response('index.html')

@csrf_exempt
def map(request):
    name = request.POST['name']
    template_values = {'name': name}
    
    return render_to_response('map.html', template_values)

def search(request):
    return render_to_response('search.html')

def missionInfo(request):
    return render_to_response('mission_info.html')

def mapManage(request):
    mapList = MapManagerIns.getMapList()
    template_values = {'result': mapList}
    return render_to_response('map_manage.html', template_values)

def mapAdd(request):
    return render_to_response('map_add.html')

@csrf_exempt
def mapAddPro(request):
    map = Map(
              name = request.POST['name'],
              map_x = int(request.POST['map_x']),
              map_y = int(request.POST['map_y']),
              map_danger1_x = int(request.POST['map_danger1_x']),
              map_danger1_y = int(request.POST['map_danger1_y']),
              map_danger2_x = int(request.POST['map_danger2_x']),
              map_danger2_y = int(request.POST['map_danger2_y']),
              map_danger3_x = int(request.POST['map_danger3_x']),
              map_danger3_y = int(request.POST['map_danger3_y']),
              date = timezone.now()
              )
    
    MapManagerIns.addMap(map)
    
    url = '/map_manage'
    return HttpResponseRedirect(url)

@csrf_exempt
def mapDelete(request):
    logging.info(request.body)
    data = json.loads(request.body)
    key = data['key']
    
    MapManagerIns.deleteMap(key)
    
    url = '/map_manage'
    return HttpResponseRedirect(url)

def robot(request):
    robotList = RobotManagerIns.getRobotList()
    template_values = {'result': robotList}
    
    return render_to_response('robot.html', template_values)

def robotSelectForm(request):
    robotList = RobotManagerIns.getRobotList()
    template_values = {'result': robotList}
    
    return render_to_response('robot_select.html', template_values)

def robotAdd(request):
    return render_to_response('robot_add.html')

@csrf_exempt
def robotAddPro(request):
    robot = Robot(
                  name = request.POST['name'],
                  serial = int(request.POST['serial']),
                  data = timezone.now()
                  )
    
    RobotManagerIns.addRobot(robot)
    
    url = '/robot'
    return HttpResponseRedirect(url)

        
