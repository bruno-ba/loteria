import scrapy
xpath = "/html/body/table/tr/td[position() < 8]//text()"


class QuinaSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://loterias.caixa.gov.br/wps/portal/loterias/landing/quina/!ut/p/a1/jc69DoIwAATgZ_EJepS2wFgoaUswsojYxXQyTfgbjM9vNS4Oordd8l1yxJGBuNnfw9XfwjL78dmduIikhYFGA0tzSFZ3tG_6FCmP4BxBpaVhWQuA5RRWlUZlxR6w4r89vkTi1_5E3CfRXcUhD6osEAHA32Dr4gtsfFin44Bgdw9WWSwj/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0K85260Q5OIRSC420O4/res/id=historicoHTML/c=cacheLevelPage/=/'
    ]

    def parse(self, response):
        body_sel = scrapy.Selector(response)

        count = 0
        resultados = []
        resultado = []
        for quote in body_sel.xpath("/html/body/table/tr/td[position() < 8]//text()").extract():
            resultado.append(quote)
            if len(resultado) == 7:
                resultados.append(resultado)
                resultado = []

