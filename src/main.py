import argparse
from loader import load_records
from report_builder import build_report
from writer import save_report

def parse_args():

    parser = argparse.ArgumentParser(
        description="description"
    )
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    parser.add_argument("--title", type=str, default="Data Report")
    parser.add_argument("--preview-limit", type=int, default=5)
    return parser.parse_args()

def main():
    args = parse_args()
    records = load_records(args.input_file)
    report = build_report(args.title, args.input_file, records, args.preview_limit)
    print(report)
    save_report(args.output_file, report)
    

if __name__ == "__main__":
    main()