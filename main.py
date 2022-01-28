"""Module collect installed apps and run or reload. """

import asyncio
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    from meeseeks import manage, settings

    settings.INSTALLED_APPS = [
        'meeseeks.MeeseeksBaseApp',
        'happy_birthder.HappyBirthder',
    ]

    asyncio.run(manage.main())
