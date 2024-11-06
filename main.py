# main.py
import os
import subprocess
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from portfolio_builder import fill_data, update_component

app = FastAPI()

# Define request schemas for validation
class HeroData(BaseModel):
    name: Optional[str] = None
    des: Optional[str] = None

class WorkData(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    duration: Optional[str] = None
    description: Optional[str] = None

class ProjectData(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    liveLink: Optional[str] = None
    codeLink: Optional[str] = None

class AboutData(BaseModel):
    description: Optional[str] = None
    skills: Optional[List[str]] = None
    personalDetails: Optional[dict] = None

class ContactData(BaseModel):
    LinkedIn: Optional[str] = None
    Twitter: Optional[str] = None
    Github: Optional[str] = None
    Email: Optional[str] = None

class DataRequest(BaseModel):
    Hero: Optional[HeroData] = None
    Work: Optional[List[WorkData]] = None
    projectData: Optional[List[ProjectData]] = None
    aboutData: Optional[AboutData] = None
    contact: Optional[ContactData] = None

class ComponentUpdateRequest(BaseModel):
    component_name: str
    prompt: str

# Endpoint to fill data
@app.post("/fill-data/")
async def api_fill_data(data_request: DataRequest):
    result = await fill_data(data_request.dict(exclude_none=True))
    return result

# Endpoint to update a specific component
@app.post("/update-component/")
async def api_update_component(request: ComponentUpdateRequest):
    result = await update_component(request.component_name, request.prompt)
    if result["status"] == "error":
        raise HTTPException(status_code=404, detail=result["message"])
    return result

# Root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the Portfolio API!"}

@app.get("/project/")
async def clone_project():
    repo_url = "https://github.com/Harsh-deepsingh/Templates-.git"
    try:
        result = subprocess.run(["git", "clone", repo_url], check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error cloning repository:", e.stderr)