import asyncio
import websockets


async def server(websocket, path):
    # This function handles incoming messages from clients
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send("Server received your message")


# Start the server
start_server = websockets.serve(server, "localhost", 8765)

# Run the server until it is closed
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
