# FastAPI Application

This repository contains a FastAPI application.

## Getting Started

To get started with this FastAPI application, follow these steps:

### Prerequisites

Make sure you have Docker installed on your machine. You can download Docker from [https://www.docker.com/get-started](https://www.docker.com/get-started).

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/abhayiitbhu/fastapi_github_app.git
cd fastapi_github_app
```

### Build and Run with Docker
Build the Docker image for the FastAPI application:

```
docker build -t fastapi-app .
```

Run the Docker container with the FastAPI application:

```
docker run -d -p 8000:8000 fastapi-app
```


