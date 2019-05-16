from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re


def clean(html):
    # Cleans HTML to remove scripts and styling, which is irrelevant to what is searched
    soup = BeautifulSoup(html, "html.parser")
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    return text


def perform_search(query):
    results = []
    for s in search(query=query, stop=5, pause=2):
        # Get cleaned result of the link returned by google search
        result = clean(requests.get(s).text)
        result = " ".join(re.split("\n{2,}", result, flags=re.UNICODE))
        result = re.split('\n', result)
        current_paragraph = ""
        has_points = 0
        # Choosing the appropriate paragraph to represent the searched website.
        # The paragraph chosen is the one with the most words contained in the search query.
        for paragraph in result:
            points = 0
            para_len = len(re.findall(r'\w+', paragraph))  # remove redundant whitespace
            if para_len < 10:  # No division by 0, no "trivial" paragraphs
               continue
            for q in query.split(' '):
                word = ' ' + q + ' '
                points += paragraph.lower().count(word.lower())
            points /= len(re.findall(r'\w+', paragraph))
            if points > has_points:
                has_points = points
                current_paragraph = paragraph
        results.append({"site": s, "summary": current_paragraph})
    return results


if __name__ == "__main__":
    to_google = input("Enter search query: ")
    print(perform_search(to_google))
