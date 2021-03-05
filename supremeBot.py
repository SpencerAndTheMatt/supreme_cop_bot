# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 13:54:31 2021

@author: SpencerAndTheMatt

supremeBot

Programme designed to acquire an item for supreme, quicker than a human
operator could (theoretically).

Made using this tutorial:
    https://www.youtube.com/watch?v=g7OfdyKFvAk
    
Example for this product:
    https://www.supremenewyork.com/shop/pants/xfa976mqy/bz829pruk

Product choice mainly due to the low probability of it selling out
Full description of product here if link goes dead:
    Work Pant
    Black
    
    Heavy cotton blend twill with enzyme wash. Slanted front pockets,
    zip fly, single coin pocket and snap closure on back pocket.
"""

#Define imports
import requests
import bs4
from splinter import Browser

#Define supremeBot class
class SupremeBot:
    
    #Define constructor
    def __init__(self, **info): #Constructor with self and info dictionary
        self.base = 'https://www.supremenewyork.com/'
        self.shop_ext = 'shop/all/'
        self.checkout_ext = 'checkout/'
        self.info = info

    #Define browser initiation method
    def init_browser(self):
        self.b = Browser() #Initiate with defaults, i.e firefox
        
    #Define find products method
    def find_product(self): #Need to use requests/bs4 before splinter because splinter is slower
        r = requests.get('{}{}{}'.format(self.base, self.shop_ext, self.info['category'])).text
        soup = bs4.BeautifulSoup(r, 'lxml')
        
        #Create 2 empty lists
        #No memory management as we don't know the final size of the lists
        tempTuple = []
        tempLink = []
        
        #Loop through to find the links with info but also with colour
        #So check name, check colour
        for link in soup.find_all('a', href=True): #Search link tags on the html code of site
            tempTuple.append((link['href'], link.text))
        
        for i in tempTuple:
            if i[1] == self.info['product'] or i[1] == self.info['color']:
                tempLink.append(i[0])
        
        #List comprehension, loops over all saved links then checks in list if there's 2 equal links
        self.finalLink = list(set([x for x in tempLink if tempLink.count(x) == 2]))[0] #Grab first element in list
        print(self.finalLink)

    #Define visit site method
    def visit_site(self):
        self.b.visit('{}{}'.format(self.base, str(self.finalLink))) #Visit website and item link
        self.b.find_option_by_text(self.info['size']).click() #Click on item
        self.b.find_by_value('add to basket').click() #Add item to basket
        
    #Define checkout method
    def checkout_function(self):
        self.b.visit('{}{}'.format(self.base, self.checkout_ext))
        #Fill in name, address, email, phone
        self.b.fill('order[billing_name]', self.info['namefield'])
        self.b.fill('order[email]', self.info['emailfield'])
        self.b.fill('order[tel]', self.info['phonefield'])
        self.b.fill('order[billing_address]', self.info['addressfield'])
        self.b.fill('order[billing_city]', self.info['city'])
        self.b.fill('order[billing_zip]', self.info['zip'])
        
        #Fill in card details
        #self.b.select('credit_card_type', self.info['card'])
        self.b.fill('credit_card[cnb]', self.info['number'])
        self.b.select('credit_card[month]', self.info['month'])
        self.b.select('credit_card[year]', self.info['year'])
        self.b.fill('credit_card[ovv]', self.info['ccv'])
        
        #Agree to terms and conditions
        self.b.find_by_css('.terms').click()
        
        '''
        The process payment part is below this comment
        Just want to highlight if you uncomment the line below to 
        process payment and run the bot, you might end up buying
        something
        '''
        #self.b.find_by_value('process payment').click()
        
    #Define main method, i.e run bot
    def main(self):
        self.init_browser()
        self.find_product()
        self.visit_site()
        self.checkout_function()


#Billing address, product info, size, etc
if __name__ == '__main__':
    INFO = {
        'driver': 'geckodriver',
        'product': 'Work Pant',
        'color': 'Black',
        'size': '36',
        'category': 'pants',
        'namefield': 'My name',
        'emailfield': 'myEmail@email.com',
        'phonefield': '01 234 456 789',
        'addressfield': '3',
        'city': 'St. Albans',
        'zip': 'AL1 1SP',
        'country': 'uk',
        'card': 'Credit Card',
        'number': '1234123412341234',
        'month': '01',
        'year': '2023',
        'ccv': '123'
        }
    bot = SupremeBot(**INFO)
    bot.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    