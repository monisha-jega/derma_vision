# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import Http404

# Create your views here.

from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.template import loader
import os, json
import tester

def index(request):
	
	context = {'jsdata' : ""}

	
	fobj = request.FILES # here you get the files needed
	if(len(fobj) != 0):
		f = fobj['sentFile']
		os.remove('tmp/test_image.jpg')
		path = default_storage.save('tmp/test_image.jpg', ContentFile(f.read()))
		jsdata = json.dumps({"res" : tester.test('tmp/test_image.jpg')})
		pr = tester.test('tmp/test_image.jpg')
		context = {'jsres' : pr[0], 'jstreat' : pr[1]}
		return render(request, 'diagnosis/result.html', context)
	else:
		return render(request, 'diagnosis/index.html', context)
	
	
# def myview(request):

	
	
