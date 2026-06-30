def save_report(output_file, report):
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(report)