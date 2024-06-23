from random import choice

capital = "Sacramento"
bird = "Valley Quail"
flower = "Golden Poppy"
song = "I Love You, California"

def random_fact():
    facts = [
     "California has the largest economy and local market in the United States, and if it were its own country, it would have the sixth largest economy in the world. Small businesses make up the majority of businesses in the state and employ millions of people.",
     "The California poppy is the state flower, and the California redwood is the state tree. The poppy was chosen in 1903 as a nod to California's gold rush history, and the redwood has been the state tree since 1937.",
     "California is one of the most racially and ethnically diverse states in the country, with over one in four Californians born overseas. The state's economic opportunities have attracted people from all over the world.",
     "California experiences over 100,000 earthquakes each year, and some research suggests that at least one earthquake occurs every three minutes in Southern California.",
     "California is home to Silicon Valley, wetsuits, Barbie dolls, fortune cookies, and almonds. The state's motto is \"Eureka!\""
    ]

    index = choice("01234")
    print(facts[int(index)])

if __name__ == "__main__":
    random_fact()