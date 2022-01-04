import os
dirPath = r"C:\Users\pozu8\Downloads"
result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
print(result)

