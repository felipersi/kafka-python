# kafka-python

Based on [Kafka-pyhton docs](https://kafka-python.readthedocs.io/en/master/index.html) and
[Kafka docs](https://kafka.apache.org/documentation/).

Install project
````console
$ git clone
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
````

Create some topic on your Kafka cluster
```console
$ ./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic numtest
```

List topics
```console
$ ./bin/kafka-topics.sh --zookeeper localhost:2181 --describe
```

Run producer
```console
$ python producer.py
```

Run consumer
```console
$ python consumer.py
```
