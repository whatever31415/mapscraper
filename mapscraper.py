from selenium import webdriver

print("Loading the browser...")
url = "https://www.google.com/maps/search/grocery+in+Mostar"
browser = webdriver.Chrome()
browser.get(url)
n = 0
input("Click Enter to continue...")
elements = browser.find_elements_by_class_name("place-result-container-place-link")
for text in elements:
    names = elements[n].get_attribute("aria-label")
    print(names)
    n += 1

#Ovo je bukvalno sve
#Da bi ucitao sto vise objekata prvo prelistaj u google maps prema dole da ih se vise ucita pa onda pritisni enter da nastavis
#Ako hoces da promijenis grad promijenis ga u linku
#Da promijenis vrstu objekta koji trazis isto promijnis u linku ali na engleskom
