import os
import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from dotenv import load_dotenv
load_dotenv()

RABBITMQ = os.environ['RABBITMQ']

rabbitmq_broker = RabbitmqBroker(url=RABBITMQ)
dramatiq.set_broker(rabbitmq_broker)


@dramatiq.actor(max_retries=1, broker=rabbitmq_broker)
def send_comment_dramatiq(name, email, message):
    from the_onahs.web_pages.services import send_comment_func
    send_comment_func(name, email, message)
