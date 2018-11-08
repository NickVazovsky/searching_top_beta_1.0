import asyncio
import requests


class Resultsasync(object):
    robots = ''
    sitemap = ''
    redirect = ''


async def gr1(url):
    r = requests.get(url+'/robots.txt')
    result = Resultsasync
    if r.status_code is 200:
        result.robots='Ok'
    else:
        result.robots = 'No'
    await asyncio.sleep(0.1)
    print(r.status_code)


async def gr2(url):
    r = requests.get(url + '/sitemap.xml')
    result = Resultsasync
    if r.status_code is 200:
        result.sitemap = 'Ok'
    else:
        result.sitemap = 'No'
    await asyncio.sleep(0.1)
    return r.status_code


async def gr3(url):
    r = requests.get(url)
    result = Resultsasync
    if r.status_code is 200:
        result.redirect = 'Ok'
    else:
        result.redirect = 'No'
    await asyncio.sleep(0.1)
    return r.status_code








def start(url, short):
    url1 = url.split("://")

    www_url = url1[0] + '://www.' + short
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [
    loop.create_task(gr1(url1[0]+"://"+short)),
    loop.create_task(gr2(url1[0]+"://"+short)),
    loop.create_task(gr3(www_url)),

    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()