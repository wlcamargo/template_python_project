from dotenv import load_dotenv
import os

load_dotenv()

var = os.getenv('VARIABLE')

print(var)