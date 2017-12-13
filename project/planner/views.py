from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View
import pprint

from rest_framework import generics, permissions
from rest_framework.renderers import JSONRenderer
# from rest_framework.views import View

from planner.wrapper import Wrapper
from planner.serializers import FlightSearchSerializer
from project.local_settings import APIAuthentication


class FlightSearchAPIListView(View):

		#Call the wrapper
		#save the response in a variable
		#parse the response for the data you want if needed (unlikely here)
		#send the data to the browser
		#cache the results if possible (do later)

	# serializer_class = FlightSearchSerializer
	# permission_classes = (permissions.AllowAny,)


	def get(self, request):
		# print(request)
		# print(dir(request))
		# print(request.body)
		# print(request.GET)
		wrapper = Wrapper(
			username = APIAuthentication.USERNAME, 
			password = APIAuthentication.PASSWORD
		)

		serializer = FlightSearchSerializer(data=request.GET)
		if serializer.is_valid():
			print(serializer.data)

			flight_search_request = serializer.flight_search_parser()
			response_version = serializer.response_parser()
			# pp = pprint.PrettyPrinter()
			# pp.pprint(json_obj)
			# print(json_obj
			print(serializer.data["response_version"], "YESSSSSSS")
			search = wrapper.flight_availability_search(response_version, flight_search_request)

			print(search)
			return JsonResponse(search)
		else:
			return JsonResponse(serializer.errors, status=405)


# class SavedFlightListView(generics.ListCreateAPIView):
# 	'''
# 	Change permission to only be if authenticated?
# 	'''
# 	queryset = SavedFlightSearch.objects.all()
# 	serializer_class = SavedFlightSearchSerializer
# 	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# 	def perform_save(self, serializer):
# 		serializer.save(user=self.request.user)	



			