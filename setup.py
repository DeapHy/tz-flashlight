from setuptools import find_packages, setup

install_requires = [
    'click==8.1.3',
    'uvicorn==0.20.0',
    'websockets==10.4',
    'fastapi==0.91.0'
]

setup(
    name='tz-flashlight',
    version='0.1.1',

    description='Реализация фонаря, управляемого по сети',

    url='https://github.com/DeapHy/tz-flashlight',

    author='Maxim Mentus',
    author_email='maksimmentus@mail.ru',

    entry_points={
        'console_scripts': [
            'tzf = tz_flashlight.cli:cli',
        ]
    },
    packages=find_packages(exclude=('tests', 'tests.*')),

    install_requires=install_requires
)