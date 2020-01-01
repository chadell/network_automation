                                                      +------+
Data Modeling Language  +--------->                   | YANG |
                                                      +------+

                                                 +---------------+
Data Modeling Schema    +--------->              |YANG Data Model|
                                                 +---------------+

                                              +---+    +----+   +--------+
Encoding/Serialization  +--------->           |XML|    |JSON|   |Protobuf|
                                              +---+    +----+   +--------+

                                         +-------+   +--------+    +---------+
Protocol                +--------->      |NETCONF|   |RESTCONF|    |gNMI/gRPC|
                                         +-------+   +--------+    +---------+

                                        +------------+  +---+  +------------+
 Orchestration          +--------->     |OpenDaylight|  |NSO|  |YANG Dev Kit|
                                        +------------+  +---+  +------------+

                                      +------+  +------+   +-+   +------+  +----+
 Programming Language   +--------->   |Python|  |Erlang|   |C|   |Golang|  |Java|
                                      +------+  +------+   +-+   +------+  +----+
