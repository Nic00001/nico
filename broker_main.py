
import logging
import asyncio
from hbmqtt.broker import Broker


logger = logging.getLogger(__name__)

config = {
    'listeners': {
        'default': {
            'type': 'tcp',
            #'bind': '127.0.0.1:9999',    # 0.0.0.0:1883  raspberry pie: 192.168.55.107 -p8869
            'bind': '192.168.55.105:9999',
            'max-connections': 50000,
        },
    },
    'sys_interval': 10,
    'topic-check': {
        'enabled': True,
        'plugins': ['topic_taboo'],
    }
}

broker = Broker(config)

@asyncio.coroutine
def startBroker():
    yield from broker.start()

if __name__ == '__main__':
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter)
    asyncio.get_event_loop().run_until_complete(startBroker())

    asyncio.get_event_loop().run_forever()