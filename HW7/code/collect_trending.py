import argparse
from bs4 import BeautifulSoup as BS
import subprocess
import os.path
import json

script_path = os.path.dirname(__file__)
raw_path =  os.path.join(script_path, '..', 'data')

def scrape(json_file):
    with open('../data/index.html', 'r') as f:
        html_content = f.read()

        soup = BS(html_content, 'html.parser')
        panel = soup.select_one('.pm-cover-stories')
        news_elements = panel.select('.postmedia-image__link')
        articles_data = []
        for e in news_elements:
            #get the link to the news article
            news_link = e.get('href')
            # cache the file
            output_file = os.path.join(raw_path, 'page.html')
            subprocess.run(["curl", "-sS", "-o", output_file, news_link], check=True)

            #Scrape the news article and add the information
            articles_data.append(scrape_news(output_file))

    #Now dump in the json file
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(articles_data, f, indent=4, ensure_ascii=False)


def scrape_news(input_file):
    with open(input_file, 'r') as f:
        html_content = f.read()
        soup = BS(html_content, 'html.parser')
        #get article info
        title = soup.select_one('.postmedia-article-topper__headline').get_text(strip=True)
        publication_date = soup.select_one('.author-meta__date').get_text(strip=True)
        author = soup.select_one('.author-meta__author').get_text(strip=True)
        blurb = soup.select_one('.postmedia-article-topper__excerpt').get_text(strip=True)

        article = {
            'title': title,
            'publication_date': publication_date,
            'author': author,
            'blurb': blurb,
        }

        return article


def main():
    parser = argparse.ArgumentParser()
    #create the argument and flag
    parser.add_argument('-o', '--output', type=str, help='path to output file')
    args = parser.parse_args()


    scrape(args.output)


if __name__ == '__main__':
    main()