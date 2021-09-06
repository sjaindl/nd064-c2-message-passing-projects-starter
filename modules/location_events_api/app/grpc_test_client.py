import grpc
import locations_pb2
import locations_pb2_grpc

import time

#time.sleep(15)

# Simulates sending of coordinates from e.g. a mobile device
print("Sending coordinates")

channel = grpc.insecure_channel("modules_kafka_1:9093")
stub = locations_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
first_location = locations_pb2.Location(
    person_id="5",
    latitude=47.0707,
    longitude=15.4395
)

print("Send coordinate 1 .. ")

stub.Create(first_location)

second_location = locations_pb2.Location(
    person_id="6",
    latitude=37.7749,
    longitude=122.4194
)

print("Send coordinate 2 ..")

stub.Create(first_location)

print("Coordinates sent ..")
