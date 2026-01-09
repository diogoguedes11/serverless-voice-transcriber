import functions_framework
import vertexai
from vertexai.generative_models import GenerativeModel, Part
from google.cloud import storage
import os


@functions_framework.cloud_event
def proccess_audio(cloud_event):
    print("hello world")
