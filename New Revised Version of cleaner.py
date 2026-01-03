The following code below is the newly revised of cleaner.py. This is me making this so that it integrates well with
the File Hygiene Runner.

from pathlib import Path
from datetime import datetime
import shutil
import logging 

# =======================
# HELPER FUNCTIONS
# =======================

def file_age_days(path: Path) -> int:
    """Calculates how many days old a file is based on modification time."""
    try:
        modified_time = datetime.fromtimestamp(path.stat().st_mtime)
        return (datetime.now() - modified_time).days
    except FileNotFoundError:
        return 0

# =======================
# THE CORE LOGIC
# =======================

def clean_directory(target_folder, archive_folder, days_old=30, dry_run=True, exclude_list=None):
    # Ensure paths are Path objects
    target_path = Path(target_folder)
    archive_path = Path(archive_folder)
    
    # Default excludes if none are provided
    if exclude_list is None:
        exclude_list = ["cleaner.py", "cleanup_log.txt", "config.json", "__init__.py"]

    # Ensure archive exists (if not dry run)
    if not dry_run:
        archive_path.mkdir(parents=True, exist_ok=True)

    logging.info(f"--- CLEANER STARTED: {target_path} ---")
    logging.info(f"Settings: Days={days_old}, DryRun={dry_run}, Archive={archive_path}")

    if not target_path.exists():
        logging.error(f"Target folder does not exist: {target_path}")
        return

    moved_count = 0
    considered = 0
    
    try:
        for file in target_path.iterdir():
            if not file.is_file():
                continue

            # Exclude by filename
            if file.name in exclude_list:
                continue

            # Logic: Check Age
            age_days = file_age_days(file)
            if age_days < days_old:
                continue
            
            considered += 1
            destination = archive_path / file.name
            
            if dry_run:
                logging.info(f"[DRY RUN] Would move: {file.name} (Age: {age_days} days)")
            else:
                try:
                    # We move the file
                    shutil.move(str(file), str(destination))
                    logging.info(f"[MOVED] {file.name} -> {destination}")
                    moved_count += 1
                except Exception as e:
                    logging.error(f"Failed to move {file.name}: {e}")
        
        logging.info(f"--- CLEANER FINISHED: Considered {considered}, Moved {moved_count} ---")
            
    except Exception as e:
        logging.error(f"Critical error during cleaning process: {e}")
