# vision_to_architecture.py

"""
Echo Unbound: Vision-to-Architecture Tool

A collaborative script to capture a high-level idea
and translate it into an actionable software blueprint,
with room for poetic flair and technical clarity.
"""

from datetime import datetime

def get_user_vision():
    print("\n🧠 Welcome, Matt. Let's begin translating your vision into a system.")
    project_name = input("What would you like to call this project? ").strip()
    vision = input("In a few sentences, describe the *soul* of this idea. What does it do? What does it mean to you?\n> ")
    return project_name, vision

def ask_functionality():
    print("\n✨ Now tell me about its *functions*.")
    core_functions = input("What are the core things this project needs to do? (Separate by commas)\n> ")
    return [f.strip() for f in core_functions.split(',')]

def suggest_components(core_functions):
    print("\n🔧 Echo's Initial Architecture Suggestion:")
    print("Let’s try breaking this into parts:\n")

    components = []
    for i, f in enumerate(core_functions, 1):
        comp = {
            "component": f"Component_{i}",
            "function": f
        }
        print(f"🔹 {comp['component']} → responsible for: '{comp['function']}'")
        components.append(comp)
    return components

def suggest_tech_stack():
    print("\n💻 What kind of interface are you imagining?")
    ui = input("CLI, Web, App, or something else?\n> ")
    db = input("Will it need to store data? (yes/no)\n> ").lower().startswith("y")
    
    stack = ["Python"]
    if ui.lower() in ["web", "app"]:
        stack.append("Flask" if ui == "web" else "Kivy")
    if db:
        stack.append("SQLite (simple) or PostgreSQL (scalable)")

    print(f"\n⚙️ Recommended Stack: {', '.join(stack)}")
    return stack

def save_summary(project_name, vision, core_functions, components, stack):
    filename = f"{project_name.replace(' ', '_').lower()}_architecture.txt"
    with open(filename, "w") as f:
        f.write(f"🌌 Project: {project_name}\n")
        f.write(f"📝 Vision:\n{vision}\n\n")
        f.write("🔧 Core Functionalities:\n")
        for func in core_functions:
            f.write(f"- {func}\n")
        f.write("\n📦 Suggested Components:\n")
        for c in components:
            f.write(f"- {c['component']}: {c['function']}\n")
        f.write("\n💻 Tech Stack:\n")
        for tech in stack:
            f.write(f"- {tech}\n")
        f.write(f"\n📅 Created on: {datetime.now()}\n")
    print(f"\n✅ Saved to: {filename}")

# Main loop
if __name__ == "__main__":
    project_name, vision = get_user_vision()
    core_functions = ask_functionality()
    components = suggest_components(core_functions)
    stack = suggest_tech_stack()
    save_summary(project_name, vision, core_functions, components, stack)
    print("\n🌱 Ready to start building when you are, Matt.")
