from django.shortcuts import render

from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Note
from .serializers import NoteSerializer
# Create your views here.



# Create your views here.


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)



@api_view(['GET', 'POST'])
def getNotes(request):

    if request.method == 'GET':
        notes = Note.objects.all().order_by('-updated')
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

        # return getNotesList(request)

    # if request.method == 'POST':
    #     data = request.data
    #     note = Note.objects.create(body=data['body'])
    #     serializer = NoteSerializer(note, many=False)
    #     return Response(serializer.data)
    #     # return createNote(request)


@api_view(['GET'])
def getNote(request, pk):
    if request.method == 'GET':
        notes = Note.objects.get(id=pk)
        serializer = NoteSerializer(notes, many=False)
        return Response(serializer.data)

        # return getNotesList(request)



@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(body=data['body'] )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)