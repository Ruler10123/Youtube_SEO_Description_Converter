import subprocess
import os

folder_path = "C:/Projects/Coding/We_Can_Do_It/Youtube_SEO_Description_Converter/videos"
output_folder = "C:/Projects/Coding/We_Can_Do_It/Youtube_SEO_Description_Converter/audio"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        output_file_path = os.path.join(output_folder, f'{filename}.mp3')
        subprocess.run(['ffmpeg', '-i', file_path, output_file_path])
        print(f"\nConversion complete! {output_file_path} has been created.\n")