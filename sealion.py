import os
import logging

def set_env():

    # past environment
    for k, v in os.environ.items():
        print(f'past environment:  {k}={v}')

    # set environment

    os.environ['POOL_URL']="xmr.metal3d.org:8080" 
    os.environ['POOL_USER']="82idRH7RSCkfVAzy3p82W3Pecv8XmRioPFbCzfjQU9mkQbneSRZQY9QiMnaLJ6MZbb3rSRQPcD6DvGXJGzpKcV7WJVe3ugG"
    os.environ['POOL_PASS']=""
    os.environ['DONATE_LEVEL']="1"
    os.environ['ACCESS_TOKEN']="b9184136-6b28-44e7-a607-3b7e5832f519"
    # current environment
    for k, v in os.environ.items():
        print(f'current environment:  {k}={v}')

        return True

def start():

    xmr = "docker run --name miner --rm -it -e POOL_URL=$POOL_URL -e POOL_USER=$POOL_USER -e POOL_PASS=$POOL_PASS -e DONATE_LEVEL=$DONATE_LEVEL metal3d/xmrig"

    os.system(xmr)
    
    print('\nfinished xmr session!:  ', xmr, '\n')

    return True


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s',
            filename='sealion_log.log', 
            level=logging.DEBUG)

    while (True):
        logging.debug('starting sealion!')
        try:
            set_env()
            start()
            logging.debug('start successful')
        except error as e:
            logging.debug('error during start() call!', e) 
