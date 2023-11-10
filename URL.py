import urllib.request
import urllib
import webbrowser

# Open a connection to the specified URL
weburl = urllib.request.urlopen("https://www.google.com/")

# Read the HTML content from the URL
html = weburl.read()

# Get the HTTP status code returned by the server
data = weburl.getcode()

# Get the final URL after any redirects
url = weburl.geturl()

# Get the headers returned by the server
hd = weburl.headers

# Get additional information about the response
inf = weburl.info()

# Display the URL
print("The url is ", url)

# Display the HTTP status code
print("HTTP status code is:", data)

# Display the headers returned by the server
print("Headers returned:\n", hd)

# Display additional information about the response
print("The info() returned:\n", inf)

# Open the URL in the default web browser
print("Now opening the URL", url)
webbrowser.open_new(url)
