import re
import os

# Файл унших, боловсруулах, бичих функц
def process_transcript_file(input_filename, output_filename):
    try:
        # Одоогийн ажлын зам
        current_directory = os.getcwd()
        print(current_directory)

        # Файл замууд
        input_file_path = os.path.join(current_directory, input_filename)
        output_file_path = os.path.join(current_directory, output_filename)

        # Оролтын файлыг унших
        with open(input_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Эхний 3 мөрийг алгасах
        lines_to_process = lines[3:]

        # Мөрүүдийг нэгтгэх
        transcript = ''.join(lines_to_process)

        # Timestamp-уудыг устгаж, текстийг үргэлжилсэн болгох
        text_without_timestamps = re.sub(r"\d{2}:\d{2}:\d{2}\.\d{3}", "", transcript)
        processed_text = " ".join(text_without_timestamps.split())

        # Үр дүнг шинэ файлд бичих
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(processed_text)
        
        print(f"Боловсруулсан текстийг {output_file_path} файлд амжилттай хадгаллаа.")
    except Exception as e:
        print(f"Алдаа гарлаа: {e}")

# Үндсэн код
input_filename = "transcriptToText/input.txt"  # Оролтын файлын нэр
output_filename = "transcriptToText/output.txt"  # Гаралтын файлын нэр

# Функцыг дуудах
process_transcript_file(input_filename, output_filename)
