from rest_framework import serializers
from .models import Flight,Reservation,Passenger


class FlightSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd"
        )

class PassangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"
class ReservationSerializer(serializers.ModelSerializer):
    passanger = PassangerSerializer(many=True)
    flight = serializers.StringRelatedField()
    flight_id = serializers.IntegerField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Reservation
        fields = ("id",'flight','flight_id',"user",'passanger')

    def create(self, validated_data):
        passenger_data = validated_data.pop("passanger")
        validated_data['user_id'] = self.context['request'].user.id
        reservation = Reservation.objects.create(**validated_data)
        for passenger in passenger_data:
            pas = Passenger.objects.create(**passenger)
            reservation.passanger.add(pas)
        reservation.save()
        return reservation

class StaffFlightSerializer(serializers.ModelSerializer):
    reservation = ReservationSerializer(many=True,read_only =True)
    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd",
            "reservation",
        )