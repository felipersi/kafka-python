from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer('numtest', bootstrap_servers=['host:9092'],
                         auto_offset_reset='earliest', enable_auto_commit=True, group_id='kafka-python-group',
                         value_deserializer=lambda x: loads(x.decode('utf-8')),
                         api_version=(0, 9))

for message in consumer:
    message = message.value
    print('{} consumed'.format(message))
