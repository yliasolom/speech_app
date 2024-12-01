from setuptools import setup

setup(
    name='speech_app',
    version='0.1',
    install_requires=[
        'torch>=2.5.1',
        'ffmpeg', 'pydub',
        'git+https://github.com/openai/whisper.git',
        'setuptools-rust',
    ],
)
