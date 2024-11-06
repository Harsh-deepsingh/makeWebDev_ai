# portfolio_builder.py
from file_utils import load_data_file, save_data_file, read_file, write_file
from ai_utils import ai
from config import FILES

async def fill_data(data_request):
    data = load_data_file()
    if "Hero" in data_request:
        hero_data = data_request["Hero"]
        data['Hero'].update(hero_data)

    if "Work" in data_request:
        data['Work'] = data_request["Work"]

    if "projectData" in data_request:
        data['projectData'] = data_request["projectData"]

    if "aboutData" in data_request:
        about_data = data_request["aboutData"]
        data['aboutData'].update(about_data)

    if "contact" in data_request:
        contact_data = data_request["contact"]
        data['contact'].update(contact_data)

    save_data_file(data)
    return {"status": "success", "message": "Data saved successfully in data.ts."}

async def update_component(component_name, prompt):
    if component_name in FILES:
        file_path = FILES[component_name]
        file_content = read_file(file_path)
        
        # Combine user prompt with existing content for AI processing
        new_content = await ai(prompt + file_content)
        write_file(file_path, new_content)
        
        return {"status": "success", "message": f"Updated {component_name.capitalize()}.tsx with new content."}
    else:
        return {"status": "error", "message": "Component not found. Please check the name and try again."}
