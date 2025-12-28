# netra/core/task_engine.py

import asyncio
from typing import Callable, Iterable, Any


class TaskEngine:
    """
    Central async execution engine.
    Controls concurrency across the framework.
    """

    def __init__(self, concurrency: int = 50):
        self.semaphore = asyncio.Semaphore(concurrency)

    async def _run_one(self, coro_func: Callable[[Any], Any], item: Any):
        async with self.semaphore:
            return await coro_func(item)

    async def run(self, coro_func: Callable[[Any], Any], items: Iterable[Any]):
        tasks = [self._run_one(coro_func, item) for item in items]
        return await asyncio.gather(*tasks)
