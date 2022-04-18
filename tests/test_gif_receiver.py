import asyncio
import unittest
from dotenv import load_dotenv

load_dotenv()

from happy_birthder import settings
from happy_birthder.happy_birthder import GifReceiver


class TestGifReceiver(unittest.TestCase):
    @staticmethod
    def async_case(func):
        async def wrapper():
            await func()
        asyncio.run(wrapper())

    def test_get_anon_id(self):
        @self.async_case
        async def body():
            gif_receiver = GifReceiver(settings.TENOR_API_KEY)
            result = await gif_receiver._get_anon_id()
            self.assertEqual(len(result), 32)

    def test_get_gif_urls(self):
        @self.async_case
        async def body():
            gif_receiver = GifReceiver(settings.TENOR_API_KEY)
            result = await gif_receiver._get_gif_urls()

            self.assertEqual(len(result), settings.TENOR_IMAGE_LIMIT)
            self.assertIn('https://media.tenor.com/images/', result[0])
