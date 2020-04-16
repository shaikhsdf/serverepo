import sys
sys.path.insert(0, './course')
from course import wsgi


app = wsgi.application