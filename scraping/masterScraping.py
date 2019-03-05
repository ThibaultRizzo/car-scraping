# import libraries
import urllib.request
from bs4 import BeautifulSoup
import re
import datetime

# Declaration
aramis_url = 'https://www.aramisauto.com/achat/recherche?page='
nb_of_page = 2
i = 0
car = {'price':None,'km_number':None,'brand':None,'new_car':None,'0_km_car':None,'used_car':None,'model':None,'car_type':None,'vendor':None,'reg_date':None,'gear_box':None,'speed_number':None,'motor_type':None,'petrol_type':None,'color':None,'doors_number':None,'vendor_link':None,'vendor_ref':None,'owner_number':None,'reg_number':None}
car_offer_keypoints = {'far-motorisation':None,'far-route':None,'far-livraison':None,'far-protection-2':None,'far-boite':None,'far-essence':None,'far-environnement':None,'far-porte':None,'far-voiture':None}
offer_keypoints_match = {'far-motorisation':('ParseString',2,2,'petrol_type','motor_type'),'far-route':('ParseDate',2,1,'reg_number'),'far-livraison':None,'far-protection-2':None,'far-boite':('ParseString',2,2,'gear_box','speed_number'),'far-essence':None,'far-environnement':None,'far-porte':('ParseDoors',1,1,'doors_number'),'far-voiture':('ParseCartType',1,3,'used_car','0_km_car','new_car')}

#functions

def SpanFindAndClean(id_name,class_Name):
    section_offer = soupcar.find('section',{'id':id_name})
    #Find Span
    if section_offer is not None:
        span = section_offer.find('span',{'class':class_Name})
        if span is not None:
            span_text = span.find_next_sibling('span').contents
            #Clean the span
            if len(span_text)>2:
                return [span_text[0].strip(),span_text[2].strip()]
            else:
                return [span_text[0].strip()]
        else:
            print('No class was found for ' + class_Name)
            return None
    else:
        print('No id was found for ' + id_name)
        return None

#ParseInt = lambda value: int(value)
#ParseDate = lambda
#ParseString = lambda value : str(value)
#ParseCartType 



#Iterate and soup the page
 
while i < nb_of_page:
    for link in BeautifulSoup(urllib.request.urlopen(aramis_url+str(i)),'html.parser').find_all('a',attrs={'class':'vehicle-info-link'}):
        #Access the page and soup the link
        soupcar = BeautifulSoup(urllib.request.urlopen('http://www.aramisauto.com'+link.get('href')),'html.parser')
        print(link.get('href'))
        car['vendor'] = 'aramisauto.com'
        car['price']=float(soupcar.find("span", id="price-car")['data-price'])
        car['car_type'] =re.findall('-\s*([\S\s]*)',soupcar.find("h1",attrs={'class':'offer-car__model'}).span.string)[0]
        #faire une fonction pour aller mettre l'url sous forme de list puis aller chercher dans la liste
        car['brand'] = re.findall('\/voitures\/([a-z0-9-]*)\/[a-z0-9-]*\/',link.get('href'))[0]
        car['model'] = re.sub('-',' ',re.findall('\/voitures\/[a-z0-9-]*\/([a-z0-9-]*)\/',link.get('href'))[0])
        car['owner_number']=re.sub('-',' ',re.findall('\/([a-z01-9]*$)',link.get('href'))[0])

        #Description du vehicule
        car_description = soupcar.find("h1",attrs={'class':'offer-car__model'}).find_all('span')
        if (len(car_description)==1):
            car['0_km_car'] = True
            car['new_car'] = car['used_car'] = False
            car['km_number']=0
        else:
            car['new_car'] = car['0_km_car'] = False
            car['used_car'] = True
            car['km_number']= int(re.sub('\s','',re.findall('- ([\d\s]*) km',str(car_description[1]))[0]))

        section_offer = soupcar.find('section',{'id':'offer-keypoints'})
        reg_date = re.findall('([0-9]{2})/([0-9]{2})/([0-9]{4})',str(section_offer.find('span',{'class':'far-route'}).find_next_sibling('span')))
        car['reg_date']= datetime.datetime.strptime(reg_date[0][0]+reg_date[0][1]+reg_date[0][2],'%d%m%Y')
        car['doors_number'] = int(re.findall(' ([1-8]) portes',str(section_offer.find('span',{'class':'far-porte'}).find_next_sibling('span')))[0])
        car['petrol_type'] = re.findall('([\S]*)<br/>',str(section_offer.find('span',{'class':'far-motorisation'}).find_next_sibling('span')))[0]
        car['motor_type'] = re.findall('<br/>([\S\s]*)</sp',str(section_offer.find('span',{'class':'far-motorisation'}).find_next_sibling('span')))[0]

        #print(soupcar.find("h1",attrs={'class':'offer-car__model'}).find_all('span')[1])
        #print(car['car_type'] =re.findall('-\s*([\S\s]*)',soupcar.find("h1",attrs={'class':'offer-car__model'}).span.string)[0])
        #print (car['reg_date'])

        
        for keypoints in car_offer_keypoints:
            car_offer_keypoints[keypoints] = SpanFindAndClean('offer-keypoints',keypoints)

        print (car_offer_keypoints)
        
        
        '''for key in list:
            el = SpanFindAndClean(key)
            if el is Not None:
                el.splice
            else: 
                print("The key " + key + " was not found")
                error_list.append(key)
        '''


    i+=1


