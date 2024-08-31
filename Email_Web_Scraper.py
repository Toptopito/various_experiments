# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:12:39 2023

@author: Vladimir Cardenas
"""

# for regular expressions
import re

# for HTTP requests
import requests

# for breaking URLS down into components
from urllib.parse import urlsplit

# for containers
from collections import deque

# for webscrapping
from bs4 import BeautifulSoup


def main():
    # provide URL here
    orig_URL = "https://members.sitegadgets.com/kingmanhigh/guestbook.html"
    
    # URLs to be scraped
    unscraped = deque([orig_URL])
    
    # initialize variable for scraped URL
    scraped = set()
    
    # initialize emails
    email_lines = set()
    
    while len(unscraped):
        # move unscraped URL to scraped
        url = unscraped.popleft() #popleft(): remove and return an element from the left side of the deque
        scraped.add(url)
        parts = urlsplit(url)
        base_url = "{0.scheme}://{0.netloc}".format(parts)
        if '/' in parts.path:
            path = url[:url.rfind('/')+1]
        else:
            path = url
        
        # send HTTP get request to website
        print("Crawling URL %s" % url)
        
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            # ignore pages with errors and continue with next URL
            continue
        
        # get email from page using regex
        # logic remove whitespace and find the Email string
        new_emails = set(re.findall(r"Email\S+", response.text.replace(" ",""), re.I))
        email_lines.update(new_emails)
        
    # loop through email lines parse to get emails
    emails = []
    for line in email_lines:
        if "pm" in line:
            line = line.split("pm")[1][1:]
            line = line.split(")")[0]
            line = line.replace("\"","")
            line_parts = line.split(",")
            if len(line_parts) == 4: # complete email address
                email= line_parts[0] + "@" + line_parts[2] + "." + line_parts[3]
                emails.append(email)
            else:
                continue
        else:
            continue
        
    emails = set(emails)
    print(emails)

    
        
    return

if __name__ == "__main__":
    main()
