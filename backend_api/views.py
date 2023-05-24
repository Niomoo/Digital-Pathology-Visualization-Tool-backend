from django.http import JsonResponse,  FileResponse, HttpResponse
from rest_framework import generics, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Project, Image, Judgement
from .serializers import UserSerializer, ProjectSerializer, ImageSerializer, JudgementSerializer
import os
import glob
# Create your views here.


@api_view(['POST'])
def sign_up(request, format=None):
  if request.method == 'POST':
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def user_list(request, format=None):
  users = User.objects.all()
  if request.method == 'GET':
    serializer= UserSerializer(users, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    user = User.objects.get(mail=request.data['mail'], password=request.data['password'])
    projects = Project.objects.filter(u_id=user.u_id)
    serializer = ProjectSerializer(projects, many=True)
    return JsonResponse({
      'message': user.u_id,
      'status': status.HTTP_200_OK
    })
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def project_list(request, pk, format=None):
  if request.method == 'GET':
    # projects = Project.objects.filter(u_id=pk)
    # serializer= ProjectSerializer(projects, many=True)
    pathPattern = "/home/nas/DZI/" + pk + r"/*.dzi"
    files = []
    for f in glob.glob(pathPattern):
      filename = f.split('/')[-1]
      name = filename.split('.')[0:2]
      files.append({
        "name": name[0] + '.' + name[1],
        "path": f
      })
    return JsonResponse(files, safe=False)

@api_view(['GET', 'POST'])
def judgement_list(request, pk, format=None):
  if request.method == 'GET':
    projects = Project.objects.filter(u_id=pk)
    images = Image.objects.filter(p_id=projects.p_id)
    judges = Judgement.objects.filter(i_id=images.i_id)
    serializer= JudgementSerializer(judges, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    user = User.objects.get(u_id=request.data['id'])
    projects = Project.objects.filter(u_id=user.u_id)
    serializer = ProjectSerializer(projects, many=True)
    return JsonResponse({
      'message': user.u_id,
      'status': status.HTTP_200_OK
    })
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def read_dzi(request, file_path):
  isImage = '_files' in file_path
  if isImage:
    with open(file_path, 'rb') as f:
      return HttpResponse(f.read(), content_type='image/jpeg')
  else:
    with open(file_path, 'rb') as f: 
      return HttpResponse(f.read(), content_type='application/xml')