from bs4 import BeautifulSoup

with open("index.html", "r") as html_file:
    # with open("archivo","r, w, ")

    content=html_file.read()
    soup = BeautifulSoup(content, "lxml")
    # esto solo hace el codigo mas legible transformandolo en string 

    courses = soup.find_all("div", class_="cards")
    

    for course in courses:
        course_name=course.h5.text
        course_price=course.a.text.split()[-1]

        print(course_name+" costs "+course_price)

    
    # tags=soup.findAll("h5")
    # #  puedes usar soup.find pero encontrara solo 1
    # #  usa soup.findAll para traer a todos
    
    # for tag in tags:
    #     print(tag.text)