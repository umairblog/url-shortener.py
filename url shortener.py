import pyshorteners
import pyshorteners.shorteners

x=input("Enter any link")
short=pyshorteners.Shortener()
shortlink=short.tinyurl.short(x)
print(shortlink)