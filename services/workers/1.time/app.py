from datetime import datetime
from time import sleep
from rsmq import RedisSMQ
from config.vars import *
from tasks import *

input_queue = RedisSMQ(host='redis-clusterip-srv', qname=APP_NAME+"_input_queue")
output_queue = RedisSMQ(host='redis-clusterip-srv', qname=APP_NAME+"_output_queue")

input_queue.createQueue(delay=0).vt(TIMEOUT).execute()
output_queue.createQueue(delay=0).vt(TIMEOUT).execute()

while True:
    sleep(DELAY)
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    try:
        msg = input_queue.receiveMessage().execute()
    except:
        continue

    # Delete Message
    input_queue.deleteMessage(id=msg['id']).execute()
    
    # Send result
    output_queue.sendMessage(delay=0).message(task(msg['message'])).execute()