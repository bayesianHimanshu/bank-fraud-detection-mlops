## Traefik

- Traefik is a modern HTTP reverse proxy and load balancer designed for containerized environments.
- WHen designing highly trafficked and scalable web systems, it is not recommended to have clients send requests directly to the application server.
- In typical web system architecture, client requests are not sent directly to the application server hosted on cloud platforms such as AWS, GCP, DigitalOcean, etc. instead, the requests are first sent to a reverse proxy server which in our case is traefik.
- Traefik will then forward the requests to the appropriate service. Then the FastAPI application will process the request and then send the response back to the traffic to the server, which in turn delivers the content to the clients browser.
- In our use case, 
    1. Automatic Service Discovery: Traefik will help with automatic service discovery, where trafik will dynamically discover services in Docker environment without manual configuration for each service. 
    2. Routing: It also helps with hostname based traffic, traefik will route incoming requests to the appropriate service based on the rules defined.
    3. SSL/TSL Termination: Traefik can handle encryption and security by managing SSL certificates and HTTPS connections, especially when we get to production.
    4. Health Checks: Health endpoint can be configured with traefik.