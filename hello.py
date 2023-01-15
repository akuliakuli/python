import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'.+src="https?://(?:www.)?youtube.com/embed/(.+?)"',s)
    if match:
        link = "https://youtu.be/" + match.group(1)
        return link
    else:
        return None


if __name__ == "__main__":
    main()