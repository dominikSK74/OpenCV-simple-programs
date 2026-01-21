import cv2

#Odczyt obrazu
img = cv2.imread('assets/image1.png', cv2.IMREAD_COLOR)
# cv2.IMREAD_COLOR - przezroczystosc ignorowana
# cv2.IMREAD_GRAYSCALE - skala szarosci
# cv2.IMREAD_UNCHANGED - kanal alfa zachowany

# W tupli () można podać sztywne rozmiary obrazu np 400x400 pikseli
# (0, 0) dajemy jeśli chcemy zrobic funkcje skalowania fx i fy
# dal fx = 0.5 i fy = 0.5 oznacza pomnożenie oryginalnych rozmiarów
# x * 0.5 i y * 0.5
img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)

# Możliwe opcje obrotu obrazu:
# cv2.ROTATE_90_CLOCKWISE
# cv2.ROTATE_90_COUNTERCLOCKWISE
# cv2.ROTATE_180
img = cv2.rotate(img, cv2.ROTATE_180)

# Zapis zmodyfikowanego obrazu
cv2.imwrite('assets/image1_rotated.png', img)

#Wyswietlenie obrazu
cv2.imshow("Window title", img)

#Czeka na nacisniecie dowolnego klawisza
# 0 - czeka w nieskonczonosc
# >0 - czeka okreslona ilosc milisekund
cv2.waitKey(0)
cv2.destroyAllWindows()