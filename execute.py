import os
import sys

# Add the parent directory of 'quiz' to the Python path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from sim.views import answer_test
from django.test import RequestFactory

def execute_code():
    request_factory = RequestFactory()
    request = request_factory.get('fake-url')
    response = answer_test(request)
    print("success executed")

if __name__ == "__main__":
    execute_code()
