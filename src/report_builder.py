def build_report(title, input_file, records, preview_limit):
    if not records:
        fields = []
    else:
        fields = records[0].keys()

    fields_text = ", ".join(fields)
    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"Source file: {input_file}")
    lines.append(f"Total records: {len(records)}")
    lines.append(f"Fields: {fields_text}")
    lines.append("")
    lines.append("## Sample records")
    
    sample_records = records[:preview_limit]

    for index, record in enumerate(sample_records, start=1):
        lines.append("")
        lines.append(f"### Record {index}")
        for key, value in record.items():
            lines.append(f"- {key}: {value}")
    
    return "\n".join(lines)