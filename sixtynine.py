#!/usr/bin/env python3

import asyncio


async def mouthful() -> int:
    """What gives 2 people each a mouthful of opportunity"""
    return 69


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        print(loop.run_until_complete(mouthful()))
    finally:
        loop.close()
