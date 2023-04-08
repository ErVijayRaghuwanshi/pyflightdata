"""
from quart import Quart, jsonify

app = Quart(__name__)

@app.route('/')
async def hello_world():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    import asyncio
    from hypercorn.config import Config
    from hypercorn.asyncio import serve

    config = Config()
    config.bind = ['localhost:8000']
    config.use_reloader = True

    asyncio.run(serve(app, config))
"""

from quart import Quart, jsonify
import asyncio
from hypercorn.config import Config as HypercornConfig
from hypercorn.asyncio import serve as hypercorn_serve
from uvicorn.config import Config as UvicornConfig
from uvicorn.workers import UvicornWorker

app = Quart(__name__)

@app.route('/')
async def hello_world():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    hypercorn_config = HypercornConfig()
    hypercorn_config.bind = ['localhost:8000']
    hypercorn_config.use_reloader = True

    uvicorn_config = UvicornConfig()
    uvicorn_config.bind = ['localhost:8001']
    uvicorn_config.workers = 4

    hypercorn_loop = asyncio.new_event_loop()
    hypercorn_loop.create_task(hypercorn_serve(app, hypercorn_config))

    uvicorn_loop = asyncio.new_event_loop()
    uvicorn_worker = UvicornWorker(uvicorn_config)
    uvicorn_loop.run_until_complete(uvicorn_worker.run())

    hypercorn_loop.run_forever()
