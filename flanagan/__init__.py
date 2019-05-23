import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv
load_dotenv(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'),
    find_dotenv()
)
app = Flask(__name__)

from .views import *  # NOQA: 402
