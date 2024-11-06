from openai import OpenAI
import openai
from dotenv import load_dotenv
import os
import json5  
import re

load_dotenv()


api_key = os.getenv("AI_API")
client = OpenAI(api_key=api_key)


files = {
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


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)



def load_data_file():
    with open(files["data"], 'r') as file:
       
        data_content = file.read()
        
        
        data_content = re.sub(r'^const data = ', '', data_content)
        
        
        data_content = re.sub(r';?\s*export\s+default\s+data\s*;', '', data_content)

       
        data_content = re.sub(r',\s*([\}\]])', r'\1', data_content)
        
        
        data = json5.loads(data_content)
        return data

def save_data_file(data):
    with open(files["data"], 'w') as file:
        file.write("const data = " + json5.dumps(data, indent=2) + ";\n\nexport default data;")


def get_user_input(prompt):
    return input(prompt).strip()


def ai(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content


def fill_data():
    
    data = load_data_file()
    
    
    hero_name = get_user_input("Enter your name for the Hero section (or press Enter to skip): ")
    if hero_name:
        data['Hero']['name'] = hero_name

    hero_description = get_user_input("Enter a description for the Hero section (or press Enter to skip): ")
    if hero_description:
        data['Hero']['des'] = hero_description

    try:
        work_count = int(get_user_input("How many work experiences would you like to include? "))
    except ValueError:
        print("Invalid input. Setting work experiences to 1 by default.")
        work_count = 1
    data['Work'] = [{"title": "", "company": "", "duration": "", "description": ""} for _ in range(work_count)]
    for i in range(work_count):
        print(f"\nWork Entry {i+1}")
        title = get_user_input("Enter job title (or press Enter to skip): ")
        if title:
            data['Work'][i]['title'] = title
        
        company = get_user_input("Enter company name (or press Enter to skip): ")
        if company:
            data['Work'][i]['company'] = company

        duration = get_user_input("Enter job duration (or press Enter to skip): ")
        if duration:
            data['Work'][i]['duration'] = duration

        description = get_user_input("Enter job description (or press Enter to skip): ")
        if description:
            data['Work'][i]['description'] = description
            
    try: 
        project_count = int(get_user_input("How many projects would you like to include? "))
    except ValueError:
        print("Invalid input. Setting work experiences to 1 by default.")
        project_count = 1       
    data['projectData'] = [{"title":"", "description": "", "liveLink":"", "codeLink":""} for _ in range(project_count)]  
    for i in range(project_count):
        print(f"\nWork Entry {i+1}")
        title = get_user_input("Enter project title (or press Enter to skip): ")
        if title:
            data['projectData'][i]['title'] = title
        
        description = get_user_input("Enter project description (or press Enter to skip): ")
        if description:
            data['projectData'][i]['description'] = description

        liveLink = get_user_input("Enter live link (or press Enter to skip): ")
        if liveLink:
            data['projectData'][i]['liveLink'] = liveLink

        codeLink = get_user_input("Enter github link (or press Enter to skip): ")
        if description:
            data['projectData'][i]['codeLink'] = codeLink
        
    about_description = get_user_input("Enter your description for the About section (or press Enter to skip): ")
    if about_description:
        data['aboutData']['description'] = about_description
        
    about_skills_input = get_user_input("Enter your skills for the About section, separated by commas (e.g., 'Java, C++, TypeScript, Python'): ")
    if about_skills_input:
    
        data['aboutData']['skills'] = [skill.strip() for skill in about_skills_input.split(',')]
        
       
    personal_location = get_user_input('Enter your personal location (or press Enter to skip): ')
    if personal_location:
        data['aboutData']['personalDetails']['location'] = personal_location
    personal_email = get_user_input('Enter your personal email section (or press Enter to skip): ')
    if personal_email:
        data['aboutData']['personalDetails']['email'] = personal_email
     
    contact_linkedIn =  get_user_input('Enter your name for the linkedIn (or press Enter to skip): ')  
    if contact_linkedIn:
         data['contact']['LinkedIn'] = contact_linkedIn
         
    contact_Twitter =  get_user_input('Enter your twitter (or press Enter to skip): ')  
    if contact_Twitter:
         data['contact']['Twitter'] = contact_Twitter
         
    contact_Github =  get_user_input('Enter your github (or press Enter to skip): ')  
    if contact_Github:
         data['contact']['Github'] = contact_Github
         
    contact_Email =  get_user_input('Enter your email (or press Enter to skip): ')  
    if contact_Email:
         data['contact']['Email'] = contact_Email
         
    save_data_file(data)

def main():
    print("Welcome! I'll help you build your portfolio website by filling in the required information.")
    
    print("Data saved successfully in data.ts.")
    
    component_change = get_user_input("Do you want to make specific changes to a component (e.g., Work.tsx)? Type 'yes' or 'no': ").lower()
    
    if component_change == "yes":
        component_name = get_user_input("Enter the component name (e.g., work, about): ").strip().lower()
        
        
        if component_name in files:
            file_path = files[component_name]
            file_content = read_file(file_path)
            
            print(f"Current content of {component_name.capitalize()}.tsx:\n{file_content}")
            
            
            new_content_prompt = get_user_input(f"Describe the changes you want in {component_name.capitalize()}.tsx: ")
            new_content = ai(new_content_prompt + file_content)
            
            
            write_file(file_path, new_content)
            print(f"Updated {component_name.capitalize()}.tsx with new content.")
        else:
            print("Component not found. Please check the name and try again.")
    
    print("Process completed.")


if __name__ == "__main__":
    main()
