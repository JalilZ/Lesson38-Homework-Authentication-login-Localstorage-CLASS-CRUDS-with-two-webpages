from django.contrib import admin

# Register your models here.
from .models import Student

admin.site.register(Student)


# username: jalil
# email: jalil@fake.com
# password: jalilpython



# Authentication1 (back-end server):
# http://127.0.0.1:8000/login/
# username: jalil
# password: jalilpython 
# >>>>>>>>>>>>>
# HTTP 200 OK
# Allow: POST, OPTIONS
# Content-Type: application/json
# Vary: Accept
#
# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NTk4OTM1OSwiaWF0IjoxNjc4MjEzMzU5LCJqdGkiOiI4OGU1MWQ1NTdlNDY0OGFjODc0MGJkMDVlZmQ1YTFiYSIsInVzZXJfaWQiOjF9.Rdl1-aDqpvv3HuBg2TLVrLY8vh4yQPgbWKf1WKJwGqU",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4MjE0MjU5LCJpYXQiOjE2NzgyMTMzNTksImp0aSI6IjMyN2FiM2U1M2YxOTQ1ZjhiNTNjYWEyNjFmNDVkODYyIiwidXNlcl9pZCI6MX0._h4VF9Dfqz49DF5NWhA2x0Ke-WOv76q-SyXRPtGqZTc"
# }


# Authentication2 (THUNDER):
# see in obsidian lesson 38