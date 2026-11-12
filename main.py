# coolest-art-01 entry (Python 3.13, standard library only).
# The art is entry.png beside this file; the program copies it to the
# output directory make.fun provides ($MAKEFUN_OUTPUT_DIR, else /output).
# The copy is byte-identical on every run: same source file, same bytes.
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
