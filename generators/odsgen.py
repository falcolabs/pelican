import pandas
import os
import glob
import csv
from xlsxwriter.workbook import Workbook


def main():
    for csvfile in glob.glob(os.path.join("results", "*.csv")):
        df = pandas.read_csv(csvfile)
        df.to_excel(f"{csvfile[:-4]}.ods")


if __name__ == "__main__":
    main()
