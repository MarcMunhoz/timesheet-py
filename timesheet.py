from docx import Document
from datetime import datetime, timedelta
import random

def generate_schedule(start_date, end_date, file_path):
    current_date = start_date
    day_count = 1

    # Open the document based on the file extension
    if file_path.endswith('.doc'):
        doc = Document()
    else:
        raise ValueError("Unsupported file format. Only .doc and .odt are supported.")

    # Iterate over each day in the given range
    while current_date <= end_date:
        day_schedule = generate_day_schedule(current_date)
        schedule_text = format_schedule_text(current_date, day_schedule)

        # Append the schedule to the document
        if file_path.endswith('.doc'):
            doc.add_paragraph(schedule_text)

        # Move to the next day
        current_date += timedelta(days=1)
        day_count += 1

    # Save the document
    doc.save("/app/output/" + file_path)

def generate_day_schedule(date):
    start_time = datetime(date.year, date.month, date.day, 9, 0)  # 09:00 AM
    lunch_start = datetime(date.year, date.month, date.day, 12, 0)  # 12:00 PM
    lunch_return = datetime(date.year, date.month, date.day, 13, 0)  # 01:00 PM
    end_time = datetime(date.year, date.month, date.day, 18, 0)  # 06:00 PM

    # Calculate the working hours with minute variations
    work_duration = (end_time - start_time) - (lunch_return - lunch_start)
    minute_variation_start = timedelta(minutes=random.randint(0, 10))
    minute_variation_lunch = timedelta(minutes=random.randint(0, 10))
    minute_variation_return = timedelta(minutes=random.randint(0, 10))
    minute_variation_end = timedelta(minutes=random.randint(0, 10))
    start_time_with_variation = start_time + minute_variation_start
    lunch_start_with_variation = lunch_start + minute_variation_lunch
    lunch_return_with_variation = lunch_return + minute_variation_return
    end_time_with_variation = end_time + minute_variation_end

    return {
        'start_time': start_time_with_variation,
        'lunch_start': lunch_start_with_variation,
        'lunch_return': lunch_return_with_variation,
        'end_time': end_time_with_variation,
        'work_duration': work_duration
    }

def format_schedule_text(date, day_schedule):
    formatted_date = date.strftime("%d/%m/%Y")
    start_time = day_schedule['start_time'].strftime("%H:%M")
    lunch_start = day_schedule['lunch_start'].strftime("%H:%M")
    lunch_return = day_schedule['lunch_return'].strftime("%H:%M")
    end_time = day_schedule['end_time'].strftime("%H:%M")
    total_work_hours = day_schedule['work_duration'].seconds // 3600

    schedule_text = f"Dia de trabalho: {formatted_date}\n"
    schedule_text += f"Chegada: {start_time}\n"
    schedule_text += f"Saída para almoço: {lunch_start}\n"
    schedule_text += f"Retorno do almoço: {lunch_return}\n"
    schedule_text += f"Saída: {end_time}\n"
    schedule_text += f"Total horas trabalhadas: {total_work_hours}\n\n"

    return schedule_text

# Example usage
start_date = datetime(2023, 5, 1)
end_date = datetime(2023, 7, 9)
file_path = 'schedule.doc'  # Change this to your desired file path

generate_schedule(start_date, end_date, file_path)
