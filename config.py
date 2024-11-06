# config.py
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AI_API")

FILES = {
    "work": "Templates-/src/components/portfolio/Work.tsx",
    "about": "Templates-/src/components/portfolio/About.tsx",
    "contact": "Templates-/src/components/portfolio/Contact.tsx",
    "hamburger": "Templates-/src/components/portfolio/Hamburger.tsx",
    "hero": "Templates-/src/components/portfolio/Hero.tsx",
    "links": "Templates-/src/components/portfolio/Links.tsx",
    "projects": "Templates-/src/components/portfolio/Projects.tsx",
    "data": "Templates-/data.ts",
    "tailwind.config": "Templates-/tailwind.config.js"
}
