import os
from pathlib import Path

# Set the directory where your pdfs are located
directory = 'D://Desktop//软考嵌入式//软考嵌入式//2006-2016下半年软考嵌入式系统设计师真题及答案'

# Create an empty list to store the extracted filenames
filenames = []


def get_filename(url):
    return url.split('/')[-1]


for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        filepath = Path(f"{filename}")

        # Extract the filename from the URL format provided
        url = f"* [{filename}](https://kurisaw.github.io/Npdf//web/viewer.html?file={get_filename(str(filepath))})"

        # Append the extracted filename to the list of filenames
        filenames.append(url)

print("Saving filenames to 'indexed-pdfs.txt'\n")
with open('indexed-pdfs.txt', 'w') as outfile:
    for filename in filenames:
        outfile.write(f"\t{filename}\n")
