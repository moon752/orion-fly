from bs4 import BeautifulSoup

def simulate_scraping():
    html = "<html><body><h1>Freelance Job</h1><p>Pay: $200</p></body></html>"
    soup = BeautifulSoup(html, "html.parser")
    title = soup.h1.text
    pay = soup.p.text
    print(f"[SIM] Scraped Title: {title}, Info: {pay}")

if __name__ == "__main__":
    simulate_scraping()
