import asyncio

async def find_divisibles(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)


        # A bit delay to give a chance for other processes
        if i % 50000 == 0:
            await asyncio.sleep(0.0001)
        

    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located


async def main():
    divs1 = loop.create_task(find_divisibles(5080000, 34113))
    divs2 = loop.create_task(find_divisibles(100052, 3210))
    divs3 = loop.create_task(find_divisibles(500, 3))
    await asyncio.wait([divs1,divs2,divs3])
    return divs1, divs2, divs3

def tasks():
    find_divisibles(5080000, 34113)
    find_divisibles(100052, 3210)
    find_divisibles(500, 3)

if __name__ == "__main__":

    #tasks()

    try:
        loop = asyncio.get_event_loop()
        loop.set_debug(1)
        d1, d2, d3 = loop.run_until_complete(main())
        print(d1.result())
    except Exception as e:
        # logging...etc
        pass
    finally:
        loop.close()
