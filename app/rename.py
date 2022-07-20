import os
files = os.listdir(r"C:\path\to\image_vector\folder")
for src in files:
    dst = src.replace(".","-",3)
    os.rename(src, dst)
