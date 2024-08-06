"""Sample code"""

import os

from dotenv import load_dotenv

load_dotenv()

var = os.getenv("VARIABLE")

print(var)
