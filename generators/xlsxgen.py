import os
import glob
import csv
from xlsxwriter.workbook import Workbook


def main():
    for csvfile in glob.glob(os.path.join("results", "*.csv")):
        workbook = Workbook(csvfile[:-4] + ".xlsx")
        worksheet = workbook.add_worksheet()
        with open(csvfile, "rt", encoding="utf8") as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()


if __name__ == "__main__":
    main()


