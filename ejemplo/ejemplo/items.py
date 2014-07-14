# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class Producto(Item):
    # define the fields for your item here like:
    # name = Field()
    titulo = Field()
    autor = Field()
    contenido = Field()
    lista_categorias = Field(serializer=str)
    lista_etiquetas = Field(serializer=str)
    pass
