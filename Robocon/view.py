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
from django.http import HttpResponse, HttpResponseRedirect
from Robocon.ImgHandler import ImgHandler
from google.appengine.api import images
from Robocon.models import Mission
from ADDON import ADDON
from ADDON import Map as MapInfo

try:
    import json
except ImportError:
    import simplejson as json

RobotManagerIns = RobotManager()
MapManagerIns = MapManager()
MissionManagerIns = MissionManager() 
    
def main(request):
    currentMissionList = MissionManagerIns.getCurrentMissionList()
    template_values = {'current': currentMissionList}
    
    return render_to_response('index.html', template_values)

@csrf_exempt
def missionAdd(request):
    name = request.POST['name']
    
    mission = Mission(name = name)
    mission.put()
    
    url = '/main'
    return HttpResponseRedirect(url)

@csrf_exempt
def map(request):
    mapList = MapManagerIns.getMapList()
    key = request.GET['key']
    
    template_values = {'result': mapList, 'key':key}
    
    return render_to_response('map.html', template_values)

@csrf_exempt
def mapSelect(request):
    key = request.POST['key']
    map_key = request.POST['selected_map_key']
    mission = MissionManagerIns.getMission(key)
    mission.map_key = map_key
    
    mission.put()
        
    url = '/mission_info?key='+key
    return HttpResponseRedirect(url)

def search(request):
    return render_to_response('search.html')

def missionInfo(request):
    key = request.GET['key']
    mission = MissionManagerIns.getMission(key)
    robot = None
    map = None
    
    if(mission.map_key != None) :
        map = MissionManagerIns.getMap(mission)
        
    if(mission.robot_key != None) :
        robot = MissionManagerIns.getRobot(mission)
        
    template_values = {'mission': mission, 'map':map, 'robot' :robot}
    return render_to_response('mission_info.html', template_values)

def mapManage(request):
    mapList = MapManagerIns.getMapList()
    template_values = {'result': mapList}
    
    return render_to_response('map_manage.html', template_values)

def mapAdd(request):
    return render_to_response('map_add.html')

@csrf_exempt
def mapAddPro(request):
    imgHandlerIns = ImgHandler()
    
    image = request.FILES['image'].read()
    
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
              map_danger4_x = int(request.POST['map_danger4_x']),
              map_danger4_y = int(request.POST['map_danger4_y']),
              map_danger5_x = int(request.POST['map_danger5_x']),
              map_danger5_y = int(request.POST['map_danger5_y']),
              map_danger6_x = int(request.POST['map_danger6_x']),
              map_danger6_y = int(request.POST['map_danger6_y']),
              map_danger7_x = int(request.POST['map_danger7_x']),
              map_danger7_y = int(request.POST['map_danger7_y']),
              map_danger8_x = int(request.POST['map_danger8_x']),
              map_danger8_y = int(request.POST['map_danger8_y']),
              map_danger9_x = int(request.POST['map_danger9_x']),
              map_danger9_y = int(request.POST['map_danger9_y']),
              map_danger10_x = int(request.POST['map_danger10_x']),
              map_danger10_y = int(request.POST['map_danger10_y']),
              date = timezone.now()
              )
    map.image = db.Blob(images.resize(image, 480))
    
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
    key = request.GET['key']
    template_values = {'result': robotList, 'key':key}
    
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

@csrf_exempt
def robotSelectPro(request):
    key = request.POST['key']
    robot_key = request.POST['selected_robot_key']
    mission = MissionManagerIns.getMission(key)
    mission.robot_key = robot_key
    
    mission.put()
        
    url = '/mission_info?key='+key
    return HttpResponseRedirect(url)

def showImage(request):
    map = db.get(request.GET['key'])
    
    #build your response
    response = HttpResponse(map.image)
    # set the content type to png because that's what the Google images api 
    # stores modified images as by default
    response['Content-Type'] = 'image/png'
    # set some reasonable cache headers unless you want the image pulled on every request
    response['Cache-Control'] = 'max-age=7200'
    return response    

@csrf_exempt
def getPath(request):
    current_x = request.GET.get("current_x")
    current_y = request.GET.get("current_y")
    dept_x = request.GET.get("dept_x")
    dept_y = request.GET.get("dept_y")
    map_key = request.GET.get("map_key")
    
    map = MapManagerIns.getMap(map_key)
    
    hazardList = [[map.map_danger1_x, map.map_danger1_y],
                  [map.map_danger2_x, map.map_danger2_y],
                  [map.map_danger3_x, map.map_danger3_y],
                  [map.map_danger4_x, map.map_danger4_y],
                  [map.map_danger5_x, map.map_danger5_y],
                  [map.map_danger6_x, map.map_danger6_y],
                  [map.map_danger7_x, map.map_danger7_y],
                  [map.map_danger8_x, map.map_danger8_y],
                  [map.map_danger9_x, map.map_danger9_y],
                  [map.map_danger10_x, map.map_danger10_y],
                  ]
    
    MapInfoIns = MapInfo(map.map_x, map.map_y, hazardList)
    
    ADDONIns = ADDON(MapInfoIns, 100)
    
    result = ADDONIns.findPath(int(current_x), int(current_y), int(dept_x), int(dept_y))
    
    data = json.dumps(result)
    
    return HttpResponse(data, content_type='application/json')
