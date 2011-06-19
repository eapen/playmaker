import time
from django.shortcuts import render_to_response


def index(request):
	return render_to_response('',{
	'payload':time.asctime( time.localtime(time.time()) )
	})


