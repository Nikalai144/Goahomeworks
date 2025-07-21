# 1) შექმენით ფუნქცია, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ ჯამს.`
def niga(a,e):
    return(a + e)
print(niga(7,1))
# 2) შექმენით ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს მისი კვადრატის მნიშვნელობას.
def zangi(a):
    return(a * a)
print(zangi(10))
# 3) შექმენით ფუნქცია, რომელიც იღებს სიას და აბრუნებს ამ სიაში უდიდეს რიცხვს.
def zangi1(y,k,o):
    if y >= k and y > o:
        return y
    elif k >= y and k >= o:
        return k
    else:
        return o
print(zangi1(10,31,87))
# 4) შექმენით ფუნქცია, რომელიც იღებს 3 რიცხვს და აბრუნებს მათ საშუალო არითმეტიკულს (sum / quantity).
def zangi2(bi):
    return((bi + bi + bi) * bi)
print(zangi2(10))
# 5) შექმენით ფუნქცია, რომელიც იღებს სიას და აბრუნებს ამ სიის შებრუნებულ ვერსიას.
def zanginame(text):
    return("ignaz")
print("ignaz")
# 6) შექმენით ფუნქცია, რომელიც იღებს სიტყვას და აბრუნებს, არის თუ არა ეს სიტყვა პალინდრომი. როგორი სიტყვებია პალინდრომი, შეგიძლიათ გაეცნოთ ქვემოთ დართულ წყაროში:
def nigaboy(nigaa):
    zangi12 = ""
    for i in nigaa:
        zangi12 = i + zangi12
    if nigaa == zangi12:
        print("palindromia")
    else:
        print("araa paindromi")

zangi = "დედა"
nigaboy(zangi)