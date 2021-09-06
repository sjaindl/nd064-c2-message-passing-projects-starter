from concurrent import futures
import grpc
import locations_pb2
import locations_pb2_grpc
from locations_pb2_grpc import LocationServiceServicer
import logging
import json
from kafka import KafkaProducer
import time

# GRPC endpoint to create locations
class LocationServicer(locations_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):

        request = {
            'person_id': request.person_id,
            'longitude': request.longitude,
            'latitude': request.latitude
        }

        print('processing request ' + request)
        producer.send(kafka_topic, json.dumps(request, indent=2).encode('utf-8'))

        return locations_pb2.Location(**request)

# TODO: Start GRPC server only once KAFKA is ready.
time.sleep(15)

kafka_url = "modules_kafka_1:9093"
kafka_topic = "locations"

print("Connecting to kafka url: " + kafka_url)
print("Sending kafka topics: " + kafka_topic)

producer = KafkaProducer(bootstrap_servers=kafka_url)

print("Started KafkaProducer")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
locations_pb2_grpc.add_LocationServiceServicer_to_server(LocationServiceServicer(), server)

print('starting on port 5000')
server.add_insecure_port('[::]:5000')
server.start()
server.wait_for_termination()
