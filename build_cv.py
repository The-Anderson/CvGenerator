import json
import os
from jinja2 import Environment, FileSystemLoader

current_dir = os.path.dirname(os.path.abspath(__file__))
file_loader = FileSystemLoader(current_dir)
env = Environment(loader=file_loader)

try:
    print("🔨 Construyendo CV...")
    template = env.get_template('template.html')
    
    with open(os.path.join(current_dir, 'cv_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    output = template.render(data)

    output_file = os.path.join(current_dir, 'Emanuel_CV.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)
        
    print(f"✅ ¡Listo! Abre el archivo: {output_file}")

except Exception as e:
    print(f"❌ Error: {e}")