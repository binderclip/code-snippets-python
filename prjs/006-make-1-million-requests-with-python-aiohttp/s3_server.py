import asyncio
from datetime import datetime
from aiohttp import web
import random


async def hello(request):
    # name = request.match_info.get("name", "foo")
    now = datetime.now().isoformat()
    delay = random.uniform(0.01, 0.8)
    await asyncio.sleep(delay)
    headers = {"content_type": "text/html", "delay": str(delay)}
    print(f"{now}: {request.path} delay: {delay}")
    body = "0.7777765323550566 0.6820758280410311 0.4466949910540329 0.4301714118515695 0.25021981851292885" \
           "0.43939880915949237 0.5380599085488146 0.01086652573727398"
    response = web.Response(body=body, headers=headers)
    return response


def main():
    # 用一样的 seed 保证每次运行效果相同
    random.seed(1)
    app = web.Application()
    app.router.add_route("GET", "/{name}", hello)
    web.run_app(app)


if __name__ == '__main__':
    main()
