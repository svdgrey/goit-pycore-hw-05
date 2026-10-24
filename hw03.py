import sys

# Parse a log line into a dictionary with date, time, level, and message.
def parse_log_line(line: str) -> dict:
    
    parts = line.strip().split(maxsplit=3)

    if len(parts) != 4:
        raise ValueError("Invalid log format.")

    date, time, level, message = parts

    if level not in ["INFO", "DEBUG", "ERROR", "WARNING"]:
        raise ValueError("Invalid log level.")

    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }

# Load logs from a file and return a list of parsed log entries.
def load_logs(file_path: str) -> list:
    logs = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                logs.append(parse_log_line(line))

    return logs

# Filter logs by a specific log level.
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"] == level.upper()]


# Count the number of logs for each log level.
def count_logs_by_level(logs: list) -> dict:
    counts = {}

    for log in logs:
        level = log["level"]

        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1

    return counts

# Display the counts of logs for each log level.
def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<18} | Кількість")
    print("-" * 18 + "-|----------")

    for level in ["INFO", "DEBUG", "ERROR", "WARNING"]:
        print(f"{level:<18} | {counts.get(level, 0)}")


def main():
    if len(sys.argv) < 2:
        print("Помилка: вкажіть шлях до лог-файлу.")
        return

    file_path = sys.argv[1]

    try:
        logs = load_logs(file_path)
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return
    except ValueError as error:
        print(f"Помилка у форматі лог-файлу: {error}")
        return
    except (OSError, UnicodeError) as error:
        print(f"Помилка читання файлу: {error}")
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2].upper()

        if level not in ["INFO", "DEBUG", "ERROR", "WARNING"]:
            print("Помилка: невідомий рівень логування.")
            return

        filtered_logs = filter_logs_by_level(logs, level)

        print(f"\nДеталі логів для рівня '{level}':")

        for log in filtered_logs:
            print(
                f"{log['date']} {log['time']} - "
                f"{log['message']}"
            )


if __name__ == "__main__":
    main()

