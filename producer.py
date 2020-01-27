from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['kfk-bhs-ovh001s.infra.azion.net:9092',
                                            'kfk-bhs-ovh002s.infra.azion.net:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number': e}
    print('{} produced'.format(data))
    producer.send('numtest', value=data)
    sleep(5)
