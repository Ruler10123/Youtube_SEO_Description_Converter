import whisper
import os

folder_path = "C:/Projects/Coding/We_Can_Do_It/Youtube_SEO_Description_Converter/audio"
output_folder = "C:/Projects/Coding/We_Can_Do_It/Youtube_SEO_Description_Converter/transcriptions"

model = whisper.load_model("medium.en")

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        output_file_path = os.path.join(output_folder, f'{filename}.txt')
        result = model.transcribe(file_path, word_timestamps=True)
        with open(output_file_path, "w") as file:
            for segment in result["segments"]:
                file.write(f"[{segment['start']:.2f}-{segment['end']:.2f}] {segment['text']}\n")
            for word in segment["words"]:
                file.write(f"  {word['word']} [{word['start']:.2f}-{word['end']:.2f}]\n")
        print(f"\nConversion complete! {output_file_path} has been created.\n")
