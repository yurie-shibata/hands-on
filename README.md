# hands-on

Sample project demonstrating Dockerized Python app with Flask.

## Development

Build the Docker image:

```bash
docker build -t hands-on .
```

Run the container:

```bash
docker run -p 8000:8000 hands-on
```

Visit <http://localhost:8000> to see the app.
