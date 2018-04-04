0. HTTPS ABC mandatory
As for project 0x07, use numbers in your answer file.

What is HTTPS?

A secure version of HTTP
A faster version of HTTP
A superior version of HTTP
Why do you need HTTPS?

To encrypt credit card and social security number information going between the client and the website servers
To encrypt all communication between the client and the website servers
To accelerate the communication between the client and the website servers
You want to setup HTTPS on your website, where shall you place the certificate?

In a secure location where nobody can access it
You can host it anywhere but you have to share the link to it on your website
On your website web server(s)

1. World wide web mandatory
Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

2. HAproxy SSL termination mandatory
“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to the next hope.

Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..
