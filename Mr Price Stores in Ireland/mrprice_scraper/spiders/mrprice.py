import scrapy


class MrpriceSpider(scrapy.Spider):
    name = "mrprice"
    allowed_domains = ["ilmontreal.com"]
    start_urls = ["https://ilmontreal.com/mr-price-ireland/"]

    def parse(self, response):
        counties = response.xpath('//h2') # since all our county names are in <h2> tags
        
        # loop over all the county names
        for county in counties[2:]: # using [2:] to avoid 'Locations' heading and a blank row
            county_name = county.xpath('span/text()').get() 
            # since there is no hierarchy between <h2> and <h3>, county and branches, we have to 
            # use the following style of xpath. 
            # areas exist within counties and they precede in <h3> after <h2>
            # following-sibling::h3: This selects all <h3> elements that are siblings to the county element 
            # (the current <h2> element) and occur after it in the document order.
            # preceding-sibling::h2[1] = $county: This condition checks if the text content of the first preceding 
            # <h2> element is equal to the value of the $county variable.
            areas = county.xpath('following-sibling::h3[preceding-sibling::h2[1] = $county]', county=county_name)
            
            if areas:  # Check if there are any areas for the current county
                for area in areas:
                    area_name = area.xpath('span/text()').get()
                    
                    yield {
                        'County': county_name,
                        'Area': area_name
                    }
            else:
                # Handle cases where no areas are found for the current county
                yield {
                    'County': county_name,
                    'Area': county_name
                }
 