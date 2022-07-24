import requests, json, csv
from bs4 import BeautifulSoup

# Hàm dùng để crawl dữ liệu
def crawl(href):
    response = requests.get("https://www.imdb.com" + href)
    soup = BeautifulSoup(response.content, "html.parser")
    # try:
    try:
        NameMovie = soup.find("div", class_="sc-94726ce4-2 khmuXj").h1.text
    except:
        NameMovie = None
    try:
        EnNameMovie_none = soup.find("div", class_="sc-94726ce4-3 eSKKHi").div.text
        EnNameMovie = EnNameMovie_none.replace("Original title: ", "")
    except:
        EnNameMovie = None
    try:
        Year = soup.find("span", class_="sc-8c396aa2-2 itZqyK").text
    except:
        Year = None
    try:
        Year_rating_runtime = soup.find("ul", class_="ipc-inline-list ipc-inline-list--show-dividers sc-8c396aa2-0 kqWovI baseAlt").text
        Rating_runtime = Year_rating_runtime.replace(Year, "")
    except:
        Rating_runtime = None
    try:
        IMDbRating = soup.find("div", class_="sc-7ab21ed2-2 kYEdvH").text
    except:
        IMDbRating = None
    try:
        CustomerRating = soup.find("div", class_="sc-7ab21ed2-3 dPVcnq").text
    except:
        CustomerRating = None
    try:
        Populary = soup.find("div", class_="sc-edc76a2-1 gopMqI").text
    except:
        Populary = None
    try:
        Genre = soup.find("div", class_="ipc-chip-list__scroller").text
    except:
        Genre = None
    try:
        Decribe = soup.find("span", class_="sc-16ede01-2 gXUyNh").text
    except:
        Decribe = None
    try:
        Director = soup.find("a", class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text
    except:
        Director = None
    try:
        Director_Writter_Star = soup.find("div", class_="sc-fa02f843-0 fjLeDR").text
        Writter_Star = Director_Writter_Star.replace("Director" + Director, "")
    except:
        Writter_Star = None
    try:
        User_reviews_none = soup.find("span", class_="three-Elements").text
        User_reviews = User_reviews_none.replace("User reviews", "")
    except:
        User_reviews = None
    try:
        UserReviews_CriticReviews_Metascore = soup.find("ul", class_="ipc-inline-list sc-124be030-0 ddUaJu baseAlt").text
        CriticReviews_Metascore = UserReviews_CriticReviews_Metascore.replace(User_reviews_none, "").replace("Critic reviews", " ").replace("Metascore", "")
    except:
        CriticReviews_Metascore = None
    movie_infor = [NameMovie, EnNameMovie, Year, Rating_runtime, IMDbRating, CustomerRating, Populary, Genre, Decribe, Director, Writter_Star, User_reviews, CriticReviews_Metascore]
    csv_writter.writerow([NameMovie, EnNameMovie, Year, Rating_runtime, IMDbRating, CustomerRating, Populary, Genre, Decribe, Director, Writter_Star, User_reviews, CriticReviews_Metascore])
    # except:
    #     movie_infor = [None, None, None, None, None, None, None, None, None, None, None, None, None]
    return movie_infor

# Mở file json để lấy list
json_file = open("./URLMovie.json", "r", encoding="utf-8")
url_movie = json.load(json_file)
url_movie = list(dict.fromkeys(url_movie))
# print(len(url_movie))

# Mở file csv để điền dữ liệu vào
csv_file = open("infor_movie.csv", "w", newline="", encoding="utf-8")
csv_writter = csv.writer(csv_file)
csv_writter.writerow(["NameMovie", "EnNameMovie", "Year", "Rating_runtime", "IMDbRating", "CustomerRating", "Populary", "Genre", "Decribe", "Director", "Writter_Star", "User_reviews", "CriticReviews_Metascore"])

# Lấy infor từng bộ movie trong list
i = 0
for link in url_movie:
    crawl(link)
    i = i + 1
    print(i)