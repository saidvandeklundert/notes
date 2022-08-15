from pathlib import Path
import shutil

current_cram = Path("cram.py")
original_cram = Path("cram_origin.py")
print("remove cram.py", current_cram.unlink())
shutil.copy(original_cram, current_cram)
