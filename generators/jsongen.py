import os
import json


def main():
    for c in os.listdir("results"):
        cn = c[:-5]
        with open(f"results/{cn}.json", "r") as f:
            with open(f"output/{cn}.json", "w") as r:
                r.write(f.read())


if __name__ == "__main__":
    main()
