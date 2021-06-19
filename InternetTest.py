"""
Tutorial Link:https://www.youtube.com/watch?v=FjT4dJ0Uq3w
"""

import speedtest

testObject = speedtest.Speedtest()

print("Getting all the nearby servers...")
testObject.get_servers()

print("Getting the Best Server...")
best_server = testObject.get_best_server()

host = best_server.get('host')
country = best_server.get('country')
latency = best_server.get('latency')

print(f'Server found at {host} in country ,{country} with a latency of {latency:.2f} ms')

print("Doing Internet Test...")

download_speed = testObject.download()
upload_speed = testObject.upload()
ping = testObject.results.ping

print(f'Download Speed = {download_speed/pow(1024,2):.2f} Mbps')
print(f'Upload Speed = {upload_speed/pow(1024,2):.2f} Mbps')
print(f'Ping = {ping:.2f} ms')
