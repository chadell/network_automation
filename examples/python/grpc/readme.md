# GRPC example

Based on https://grpc.io/docs/tutorials/basic/python/
Benchmarck https://medium.com/@shmulikamar/python-serialization-benchmarks-8e5bb700530b

## .proto file

The protofiles (`protos/route_guide.proto`) contain:

* **Service** definition, with all the **rpc** methods, *simple* or *stream*
* **Message** type definitions

From the protofile, we generate the Python classes to be used in our applications:

```
$ pip install -r requirements.txt

$ python -m grpc_tools.protoc --proto_path ./protos --python_out=. --grpc_python_out=. ./protos/route_guide.proto
```

This generates two files: `<proto_service>_pb2.py` and `<proto_service>_pb2_grpc.py`

`<proto_service>_pb2_grpc.py` exposes to our application several entities:

* classes for the messages defined in route_guide.proto
* classes for the service defined in route_guide.proto
	* `RouteGuideStub`, which can be used by clients to invoke RouteGuide RPCs
	* `RouteGuideServicer`, which defines the interface for implementations of the `RouteGuide` service
* a function for the service defined in route_guide.proto
	* `add_RouteGuideServicer_to_server`, which adds a `RouteGuideServicer` to a `grpc.Server`

> This is the "compilation" of protobuf, exposing the data/methods to application. Notice how the `DESCRIPTOR.serialized_pb` looks like, with the serialization of the data structure.
