from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from postings.models import Posting
from postings.serializers import PostingSerializer
