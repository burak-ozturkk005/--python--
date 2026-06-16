fuel = 15
distance = 40
if fuel >10 and distance < 50:
    print("Can not reach to port!")
if fuel > 5 or distance > 100:
    print("Risky")
if not (fuel == 0):
    print("Still have fuel")

#pythonda if içine illa ki karşılaştırma koymak zorunda değiliz. Bir değer kendi başına "doğru gibi" ya da "yanlış gibi" sayılır.
#Boş şyler (0, boş string"",boş liste [], None)
#False sayilir. dolu olan her şey true

bikes = []
if bikes:
    print("contains nice bikes")
else:
    print("Store empty")
