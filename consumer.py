from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer('numtest', bootstrap_servers=['kfk-bhs-ovh001s.infra.azion.net:9092',
                                                       'kfk-bhs-ovh002s.infra.azion.net:9092'],
                         auto_offset_reset='earliest', enable_auto_commit=True, group_id='kafka-python-group',
                         value_deserializer=lambda x: loads(x.decode('utf-8')),
                         api_version=(0, 9))

for message in consumer:
    message = message.value
    print('{} consumed'.format(message))
