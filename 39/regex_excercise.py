import re

with open("../../Github/itstep-ukoly/39/bazar.html", encoding="utf-8") as file:
    html = file.read()
# (html)
rx_name = re.compile(r"<h2 class=\"title\".+<")
# rx_cena = re.compile(
#    r"class=\"c-product__price c-product__price--after-discount c-price-drop__price-drop\">\n +od(.+) Kč<"
# )

nazvy = rx_name.findall(html)
# ceny = rx_cena.findall(html)
print(nazvy)
# print(len(ceny))
# for item in range(len(produkty)):
