import asyncio
import get_data as gd
import websockets

# here we'll store all active connections to use for sending periodic messages
connections = []


@asyncio.coroutine
def connection_handler(connection, path):
    connections.append(connection)  # add connection to pool
    while True:
        msg = yield from connection.recv()
        if msg is None:  # connection lost
            print("Message leer")
            connections.remove(connection)  # remove connection from pool, when client disco$
            break
        elif msg.startswith('LastDay'):
            print("Last Day call")
            msg = msg[8:]
            i = 0
            for connection in connections:
                if i == 0:
                    i++
                else:
                    msg = gd.LastDay(msg)
                print(connection)
                yield from connection.send(msg)  # send message to each connected clie$
                print('< {}'.format(msg))    # send message to each connected client
            connections.pop(1)
        elif msg.startswith('RangeData'):
            for connection in connections:
                yield from connection.send(msg)
            connections.pop(1)
        else:
            yield from connection.send(msg)
            print('> {}'.format(msg))


@asyncio.coroutine
def send_periodically():
    while True:
        yield from asyncio.sleep(5)  # switch to other code and continue execution in 5 seco$
        for connection in connections:
            print('> Periodic event happened.')
            yield from connection.send('Periodic event happened.')  # send message to each c$


start_server = websockets.serve(connection_handler, '', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.ensure_future(send_periodically())  # before blocking call we schedule our coroutine$
asyncio.get_event_loop().run_forever()


