from fastapi import FastAPI, HTTPException, Query
from typing import List
import httpx
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (adjust as needed)
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)



BASE_URL = "https://api.github.com"

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend for GitHub repositories!"}

BASE_URL = "https://api.github.com"

@app.get("/github-repos/{username}")
async def get_user_repos(username: str, page: int = Query(1, gt=0), per_page: int = Query(10, gt=0)):
    try:
        async with httpx.AsyncClient() as client:
            url = f"{BASE_URL}/users/{username}/repos"
            params = {"page": page, "per_page": per_page}
            response = await client.get(url, params=params)
            response.raise_for_status()
            repos = response.json()

            # Extract necessary repo details
            repo_names = [{"name": repo["name"]} for repo in repos]
            return repo_names

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"GitHub API error: {e}")
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Request error: {e}")

@app.get("/github-commits/{username}/{repo}")
async def get_last_commit(username: str, repo: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/repos/{username}/{repo}/commits")
            if response.status_code == 200:
                commits = response.json()
                if commits:
                    last_commit = commits[0]["commit"]
                    return {
                        "repo": repo,
                        "last_commit_author": last_commit["author"]["name"],
                        "last_commit_message": last_commit["message"]
                    }
                else:
                    raise HTTPException(status_code=404, detail="Commits not found for the repository")
            else:
                raise HTTPException(status_code=response.status_code, detail="Repository not found or API request failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch last commit: {str(e)}")