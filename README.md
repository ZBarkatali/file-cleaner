### file-cleaner ###
Automated file clean-up tool with quarantine safety!


The Python-based automation tool that I had created today (31/12/2025) is used to help safely clean up old files from a target directory by moving them into a quarantine folder instead of deleting them outright.

Built to reduce clutter, save storage, and automate file hygiene for individuals and small businesses. This is my first ever attempt on getting to know Python a little bit more and gain knowledge from it and throw myself in the deep end to start something myself.

### Features ###
- Scans a target directory for files
- Moves files into a quarantine folder (no permanent deletion)
- Simple, configurable logic
- Built with safety-first principles
- Designed for automation and future scheduling (future scheduling is something that I will work on)

### How does this work?? ###
1. Find a target folder 
2. A quarantine folder is created automatically from my code
3. Files are identified and moved safely
4. Nothing is deleted permanently... just yet!

Me doing this will help create a time-saving, money-efficient approach to allowing recovery if needed for individuals and small businesses, along with reducing risks (time, money, employees).

The following code that I used below was:

from pathlib import Path
import shutil
import sys

TARGET_FOLDER = Path(r"C:\Users\Zain\Documents\Python Work\Project")
QUARANTINE_FOLDER = TARGET_FOLDER / "quarantine"

source = TARGET_FOLDER / "wanker.txt"
dest = QUARANTINE_FOLDER / "wanker.txt"

print("RUNNING FILES:", __file__)
print("PYTHON:", sys.executable)
print("TARGET_FOLDER exists:", QUARANTINE_FOLDER.exists())
print("SOURCE:", source)
print("SOURCE exists:", source.exists())
print("DEST", dest)

QUARANTINE_FOLDER.mkdir(exist_ok=True)

try:
    shutil.move(str(source), str(dest))
    print("File moved successfully.")
except Exception as e:
    print("Move failed:", repr(e))

Once the code was made, I quickly saved it inside of my Target folder along with the file in question that I wanted to move to my Quarantine folder (the name of this Python file that I had saved is named "cleaner.py"). Once that was done, I had opened up PowerShell, entered the file path that included the target folder in question. Once I clicked enter, PowerShell opened up a new line with the file path in question, indicating that I am making a change somewhere in my file path. From there, I entered "python cleaner.py" and there with some messages that popped up, indicating that the job is valid and running - I quickly checked the target folder and I can confirm that now, this works :).
