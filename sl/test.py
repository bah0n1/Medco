from selenium import webdriver
import time
import os
from openpyxl import Workbook
from capmd import save


driver=webdriver.Firefox(executable_path=os.getcwd()+"/geckodriver")
counter = 1531
medicine_name = None
small_form=None
Generic_name=None
Strength_name=None
Manufactured_name=None
unt_price=None
pack_price=None
Indications=None
Therapeutic=None
Pharmacology=None
Dosage=None
Interaction=None
Contraindications=None
Side_Effects=None
Pregnancy=None
Precautions=None
Populations=None
Overdose=None
Storage=None
for a in range(30227,50001):
    driver.get("https://medex.com.bd/brands/"+str(a))
    titel=driver.title
    if titel == "Not Found":
        pass
    else:
        try:
            medicine_nm = driver.find_element_by_xpath("//div[@class='col-xs-12 brand-header']//span[2]").text
            small_form =  driver.find_element_by_xpath("//div[@class='col-xs-12 brand-header']//span[2]//small").text
        except:
            medicine_nm = driver.find_element_by_xpath("//div[@class='col-xs-12 brand-header']//span").text
            small_form =  driver.find_element_by_xpath("//div[@class='col-xs-12 brand-header']//span//small").text

        medicine_name = medicine_nm.replace(small_form,"")
        


        Generic_name = driver.find_element_by_xpath("//div[@title='Generic Name']").text
        
        Strength_name = driver.find_element_by_xpath('//div[@title="Strength"]').text
        
        Manufactured_name = driver.find_element_by_xpath('//div[@title="Manufactured by"]').text
        try:
        # price for bottol and tablate
            price_unt = driver.find_element_by_xpath('//div[@class="package-container"]').text
            
            # price for bottol
            if price_unt.find("bottle") > 0:
                price = driver.find_element_by_xpath('//div[@class="package-container"]').text
                
                lenth=len(price)
                for c in range(1,lenth):
                    if price[c] == ":":
                        lenth_p=c
                    else:
                        continue
                unt_price=price[lenth_p+4:]
                

                for b in range(1,5):
                    try:
                        pack_price = driver.find_element_by_xpath('//div[@class="package-container"]['+str(b)+']').text
                        
                    except:
                        continue
            elif price_unt.find("vial") > 0:
                unt_pc=price_unt[7+8:]
                if unt_pc.find("(") >=0:
                    cc=unt_pc.find("(")
                    unt_price = unt_pc[:cc-1]
                    
                else:

                    unt_price = price_unt[price_unt.find("৳")+2:]
                    
                for b in range(1,5):
                    try:
                        pack_price = driver.find_element_by_xpath('//div[@class="package-container"]['+str(b)+']').text
                        
                    except:
                        continue
            elif price_unt.find("ml ampoule") > 0:
                unt = driver.find_element_by_xpath('//div[@class="package-container"]').text[16:]
                length = unt.find("(")
                unt_price = unt[:length-1]
                
                try:
                    pack_price = driver.find_element_by_xpath('//div[@class="package-container"]//span').text[1:].replace(")","")
                    
                except:
                    pass

            elif price_unt.find("gm tube") > 0:
                unt = driver.find_element_by_xpath('//div[@class="package-container"]').text[14:]
                unt_price = unt
                pack_price = driver.find_element_by_xpath('//div[@class="package-container"]').text
                

            elif price_unt.find("ml drop") >0:

                unt_price = price_unt[price_unt.find("৳")+2:]
                pack_price= price_unt
                

            else:
                unt = driver.find_element_by_xpath('//div[@class="package-container"]').text[14:]
                length = unt.find("(")
                if length >0:

                    unt_price = unt[:length-1]
                    
                    try:
                        pack_price = driver.find_element_by_xpath('//div[@class="package-container"]//span').text[1:].replace(")","")
                        
                    except:
                        pass
                else:
                    unt_price = unt
        except:
            pass
                
        try:
            Indications = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="indications"]//parent::div//div[@class="ac-body"]').text
            
        except:
            pass
        try:
            Therapeutic = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="drug_classes"]//parent::div//div[@class="ac-body"]').text
            
        except:
            pass
        try:
            Pharmacology = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="mode_of_action"]//parent::div//div[@class="ac-body"]').text
            
        except:
            pass
        try:

            Dosage = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="dosage"]//parent::div//div[@class="ac-body"]').text
            
        except:
            pass
        try:
            Interaction = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="interaction"]//parent::div//div[@class="ac-body"]').text
            
        except:
            pass
        try:
            Contraindications = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="contraindications"]//parent::div//div[@class="ac-body"]').text
            
        except:
            pass
        try:
            Side_Effects = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="side_effects"]//parent::div//div[@class="ac-body"]').text
            
        except:
            pass
        try:
            Pregnancy = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="pregnancy_cat"]//parent::div//div[@class="ac-body"]').text
            
        except:
            pass
        try:
            Precautions = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="precautions"]//parent::div//div[@class="ac-body"]').text
            
        except:
            pass
        try:
            try:
                Populations = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="pediatric_uses"]//parent::div//div[@class="ac-body"]').text
                
            except:
                Overdose=driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="overdose_effects"]//parent::div//div[@class="ac-body"]').text
                
        except:
            pass
        try:

            Storage = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="storage_conditions"]//parent::div//div[@class="ac-body"]').text
            
        except:
            pass
        

        medicine = medicine_name
        small_form=small_form
        Generic_name=Generic_name
        Strength_name=Strength_name
        Manufactured_name=Manufactured_name
        unt_price=unt_price
        pack_price=pack_price
        Indications=Indications
        Therapeutic=Therapeutic
        Pharmacology=Pharmacology
        Dosage=Dosage
        Interaction=Interaction
        Contraindications=Contraindications
        Side_Effects=Side_Effects
        Pregnancy=Pregnancy
        Precautions=Precautions
        Populations=Populations
        if Overdose is not None:
            Overdose=Overdose
        else:
            Overdose=""
        Storage=Storage


        cc = save(counter,medicine,small_form,Generic_name,Strength_name,Manufactured_name,unt_price,pack_price,Indications,Therapeutic,Pharmacology,Dosage,Interaction,Contraindications,Side_Effects,Pregnancy,Precautions,Populations,Overdose,Storage)
        counter+=1
# https://medex.com.bd/brands/16776/acilog-100iu
# https://medex.com.bd/brands/17301/5-fu-phares-25mg