import os

# Go to parent directory
os.system("cd ..")

# Go to the AkulAI folder
os.system("cd akulai")

# Run the server for the API
os.system("uvicorn akulai:app --reload")
