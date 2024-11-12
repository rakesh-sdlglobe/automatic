import os
import subprocess
from datetime import datetime

# Path to your local git repository (replace with the actual local path)
repo_path = r"C:\Users\LENOVO\Desktop\automatic"  # Replace with your local repo path
commit_message = f"Code is committed on  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def git_commit_and_push():
    try:
        # Change to the repo directory
        os.chdir(repo_path)

        # Stage all changes
        subprocess.run(["git", "add", "."], check=True)

        # Commit the changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push to the main branch
        subprocess.run(["git", "push", "origin", "main"], check=True)

        print("Changes committed and pushed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Run the function
git_commit_and_push()
