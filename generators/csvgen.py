import os
import json


def main():
    content = {}
    for c in os.listdir("results"):
        cn = c[:-5]
        with open(f"results/{cn}.json", "r") as f:
            content[cn] = json.loads(f.read())

        with open(f"output/{cn}.csv", "w") as f:
            f.write(
                '"sbd","name","school","birthdate","math","lit","eng","gifted","totalNorm","totalGifted"\n'
                + "\n".join(
                    [
                        ",".join([repr(i) for i in list(r.values())])
                        for r in content[cn]["result"]
                    ]
                )
                + "\n"
            )
            # "sbd", "name", "school", "birthdate", "math", "lit", "eng", "gifted", "totalNorm", "totalGifted"


if __name__ == "__main__":
    main()
