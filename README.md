\## Build and Deploy with Docker Compose



\### Command

```powershell

docker compose up --build -d

```



\### Purpose

Builds the web and database images and starts both services in detached mode.



\### Observed Results

\- Web image: Built successfully.

\- Database image: Built successfully.

\- Web container: Running.

\- Database container: Healthy.



\### Verification Commands

```powershell

docker compose ps

docker compose logs --tail 50

```



\### Browser Verification

URL: http://localhost:5000



\*\*Observed result:\*\* \[Record the actual webpage content and database connection status.]



\### Conclusion

Docker Compose successfully built the application images and started the web and database services. The database health check reported a healthy status.







## Web Application Feature Update

### Modification
Added a new `/about` route to the Python web application. The page displays an About heading, a feature-update message, and a link back to the home page.

### Rebuild and Deployment
```powershell
docker compose up --build -d
```

### Verification
- Home page: http://localhost:5000
- About page: http://localhost:5000/about






## Web Application Scaling

### Command
```powershell
docker compose up -d --scale web=3
```

### Purpose
Starts three instances of the web service. Nginx acts as a reverse proxy and forwards requests to the web service.

### Verification
```powershell
docker compose ps
```

### Observed Results
The output showed three web containers (`web-1`, `web-2`, and `web-3`), one database container (`db-1`), and one proxy container (`proxy-1`).

### Browser Test
http://localhost:5000

Record the actual browser result and the container hostnames returned by repeated requests.

## Application Monitoring

### Resource Monitoring
```powershell
docker stats --no-stream
```

### Service Status
```powershell
docker compose ps
```

### Logs
```powershell
docker compose logs --tail 50
```

### Purpose
These commands display a snapshot of container resource usage, service status and health, and recent application logs.







## Monitoring Container Resources

### Command
```powershell
docker stats --no-stream
```

### Purpose
Displays a snapshot of CPU usage, memory usage, network I/O, block I/O, and process counts for running containers.

### Observed Results
The monitoring output displayed resource statistics for:
- Three web application containers
- One Nginx reverse proxy
- One PostgreSQL database container

The measured memory usage ranged from approximately 8.4 MiB for the proxy to 37.2 MiB for the database in this snapshot.

### Conclusion
Docker's built-in monitoring command was used to inspect resource consumption across the scaled application. The results provide a snapshot of container resource usage.






