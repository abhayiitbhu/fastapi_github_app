Running the Backend (FastAPI)
Clone the Repository:

bash
Copy code
git clone https://github.com/your/repository.git
cd repository-name
Build the Docker Image:

bash
Copy code
docker build -t fastapi-app .
Run the Docker Container:

bash
Copy code
docker run -d -p 8000:8000 fastapi-app
Replace 8000 with the port on which your FastAPI server is running if different.

Access the FastAPI Swagger Documentation:

Open your web browser and go to http://localhost:8000/docs to view the Swagger documentation.

