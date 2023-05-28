# 0x09-web_infrastructure_design
## An overview of what happens when you browse the web

When a user types an address into the search bar of a browser, several processes are initiated to retrieve the desired website or web page. Here's an overview of what happens:

User input: The user enters the address, also known as a URL (Uniform Resource Locator), into the search bar. The URL can be in the form of "http://" or "https://" followed by the domain name (e.g., www.alx.com) or the IP address (e.g., 192.168.0.1) of the website they want to visit.

DNS resolution: The browser first checks its local cache to see if it has the IP address corresponding to the entered domain name. If it doesn't have the information, the browser sends a DNS (Domain Name System) lookup request to a DNS server. The DNS server translates the domain name into an IP address, allowing the browser to locate the web server that hosts the website.

Establishing a connection: Once the browser has the IP address, it opens a TCP (Transmission Control Protocol) connection with the web server. This connection is established using a three-way handshake process to ensure reliable data transmission between the browser and the server.

HTTP request: After the connection is established, the browser sends an HTTP (Hypertext Transfer Protocol) request to the web server. The request includes the method (such as GET, POST, etc.), headers (additional information about the request), and the URL of the specific page or resource the user wants to access.

Server processing: The web server receives the HTTP request and processes it. It determines which web page or resource corresponds to the requested URL and prepares a response.

Server response: The web server generates an HTTP response, which includes a status code, headers (containing metadata), and the requested content. The status code indicates whether the request was successful (e.g., 200 OK) or encountered an error (e.g., 404 Not Found).

Data transfer: The server sends the HTTP response back to the browser over the established TCP connection. The response typically includes the HTML content of the web page, but it can also contain other resources like CSS stylesheets, JavaScript files, images, etc. These resources may be referenced in the HTML and are requested separately if necessary.

Rendering the page: The browser receives the response and begins parsing the HTML content. It fetches any additional resources referenced in the HTML (e.g., images, scripts) by sending additional HTTP requests to the server. The browser then processes the received data and renders the web page according to the HTML, CSS, and JavaScript instructions.

Displaying the page: Once the browser has finished rendering the web page, it displays the final result in its window. The user can now see and interact with the requested website.

Throughout this process, there may be additional complexities like caching, redirects, SSL/TLS encryption, and more, depending on the specific circumstances. However, this overview covers the fundamental steps involved in loading a website when a user types an address into the browser's search bar.