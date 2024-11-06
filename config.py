# config.py
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AI_API")

FILES = {
    "work": "templates/src/components/portfolio/Work.tsx",
    "about": "templates/src/components/portfolio/About.tsx",
    "contact": "templates/src/components/portfolio/Contact.tsx",
    "hamburger": "templates/src/components/portfolio/Hamburger.tsx",
    "hero": "templates/src/components/portfolio/Hero.tsx",
    "links": "templates/src/components/portfolio/Links.tsx",
    "projects": "templates/src/components/portfolio/Projects.tsx",
    "data": "templates/data.ts",
    "tailwind.config": "templates/tailwind.config.js"
}
