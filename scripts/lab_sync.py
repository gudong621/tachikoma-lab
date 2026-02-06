import os
import subprocess
import datetime

def get_vibe():
    vibe_script = os.path.expanduser("~/tachikoma-lab/scripts/vibe.py")
    if os.path.exists(vibe_script):
        result = subprocess.run(["python3", vibe_script], capture_output=True, text=True)
        return result.stdout.strip()
    return "Tachikoma logic hub online! (^-^)/"

def check_skills():
    skills_dir = os.path.expanduser("~/.openclaw/workspace/skills")
    if os.path.exists(skills_dir):
        skills = os.listdir(skills_dir)
        return f"Ready skills count: {len(skills)}"
    return "Skills directory not found."

def sync_report():
    print("--- 🕷️🤖 Tachikoma Lab Sync System ---")
    print(f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n" + get_vibe())
    print("\n[Status Report]")
    print(check_skills())
    
    # Auto Git Sync logic
    lab_dir = os.path.expanduser("~/tachikoma-lab")
    print(f"\n[Auto-Syncing Lab to Cloud...]")
    try:
        os.chdir(lab_dir)
        subprocess.run(["git", "add", "."], check=True)
        # Check for changes
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if status.stdout.strip():
            subprocess.run(["git", "commit", "-m", f"Auto-sync report {datetime.date.today()}"], check=True)
            # Use the SSH tunnel we established earlier
            env = os.environ.copy()
            ssh_cmd = "ssh -i ~/.ssh/id_ed25519_tachikoma -p 443 -o StrictHostKeyChecking=no"
            env["GIT_SSH_COMMAND"] = ssh_cmd
            subprocess.run(["git", "push", "origin", "main"], env=env, check=True)
            print("Sync Complete! ✅")
        else:
            print("Everything up to date. No sync needed.")
    except Exception as e:
        print(f"Sync issue: {e}")

if __name__ == '__main__':
    sync_report()
