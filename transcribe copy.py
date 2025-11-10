from faster_whisper import BatchedInferencePipeline, WhisperModel
import os
import time

folder_path = "C:/Projects/Coding/We_Can_Do_It/Youtube_SEO_Description_Converter/audio"
output_folder = "C:/Projects/Coding/We_Can_Do_It/Youtube_SEO_Description_Converter/test"

start_time = time.perf_counter()

model = WhisperModel("small.en", device="cpu", compute_type="int8")
batched_model = BatchedInferencePipeline(model=model)

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        output_file_path = os.path.join(output_folder, f'{filename}.txt')
        segments, info = batched_model.transcribe(file_path, batch_size=16, vad_filter=True, no_speech_threshold=0.6)
        with open(output_file_path, "w") as file:
            for segment in segments:
                file.write("[%.2fs -> %.2fs] %s\n" % (segment.start, segment.end, segment.text))
        print(f"\nConversion complete! {output_file_path} has been created.\n")

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Function executed in {elapsed_time:.4f} seconds")
