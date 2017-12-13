from rest_framework import serializers
from planner.models import SavedFlightSearch


class FlightSearchSerializer(serializers.Serializer):
    response_version = serializers.CharField(max_length=9, default="VERSION41")
    destination = serializers.CharField(max_length=3)
    departure_time = serializers.TimeField(default="1100")
    origin = serializers.CharField(max_length=3)
    quantity = serializers.IntegerField()
    type_of_trip = serializers.CharField(max_length=9)
    departure_date = serializers.DateField()
    return_date = serializers.DateField()

    def flight_search_parser(self):
        print("before_parser")
        if self.is_valid():
            data = self.data
            unixTC = "T00:00:00"

            segment_details = []
            departure = {}
            returnfrom = {}

            FlightSearchRequest = {}

            departure["Origin"] = data['origin']
            departure["Destination"] = data['destination']
            departure["DepartureDate"] = data['departure_date'] 
            departure["DepartureTime"] = data['departure_time']

            returnfrom["Origin"] = data['destination']
            returnfrom["Destination"] = data['origin']
            returnfrom["DepartureDate"] = data['return_date'] 
            returnfrom["DepartureTime"] = data['departure_time']
            
            segment_details.append(departure)
            segment_details.append(returnfrom)
            

            FlightSearchRequest["Adults"] = str(data['quantity'])
            FlightSearchRequest["ClassOfService"] = "ECONOMY"
            FlightSearchRequest["TypeOfTrip"] = data['type_of_trip']
            FlightSearchRequest["SegmentDetails"] = segment_details

          

            # ["ResponseVersion"] = data['response_version']
            # ["FlightSearchRequest"] = FlightSearchRequest



            return FlightSearchRequest

    def response_parser(self):

        if self.is_valid():
            data = self.data

            ResponseVersion = data['response_version']
            return ResponseVersion







class SavedFlightSearchSerializer(serializers.ModelSerializer):
    
    user = serializers.SlugRelatedField(
		many=False,
		read_only=True,
		slug_field='username'
	)

    class Meta:
        model = SavedFlightSearch
        fields = [
        	'destination', 'origin', 'quantity', 'type_of_trip', 
        	'departure_date', 'return_date', 'id', 'user'
        ]
        read_only_fields = ('id',)


#Do we need a model to base the serializer on? Examples online mostly show using a model
#Should we be using the model for saving flights? If so, is it possible to use the
#FlightSearchSerializer? Or should I make one serializer for the API request, one for saving,
#one for deserializing, etc.
#Would a ListSerializer (per DRF docs) be good for deserializing that amount of data?         