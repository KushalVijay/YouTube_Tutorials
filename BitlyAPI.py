"""
Tutorial Link:https://youtu.be/aCuf_eIfxUc
"""
import bitly_api

Access_Token = "Access_Token"

connection  = bitly_api.Connection(access_token=Access_Token)

url = input()

shorten_url = connection.shorten(url)

print(shorten_url.get('url'))
