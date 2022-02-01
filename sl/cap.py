from selenium import webdriver
import time
import os


driver=webdriver.Firefox(executable_path=os.getcwd()+"/geckodriver")

for a in range(999999):
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
        print(medicine_name)
        print(small_form)


        Generic_name = driver.find_element_by_xpath("//div[@title='Generic Name']").text
        print(Generic_name)
        Strength_name = driver.find_element_by_xpath('//div[@title="Strength"]').text
        print(Strength_name)
        Manufactured_name = driver.find_element_by_xpath('//div[@title="Manufactured by"]').text
        print(Manufactured_name)
        # price for bottol and tablate
        price_unt = driver.find_element_by_xpath('//div[@class="package-container"]').text
        print(price_unt)
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
            print(unt_price)

            for b in range(1,5):
                try:
                    pack_price = driver.find_element_by_xpath('//div[@class="package-container"]['+str(b)+']').text
                    print(pack_price)
                except:
                    continue
        elif price_unt.find("vial") > 0:
            unt_pc=price_unt[7+8:]
            if unt_pc.find("(") >=0:
                cc=unt_pc.find("(")
                unt_price = unt_pc[:cc-1]
                print(unt_price)
            else:

                unt_price = price_unt[price_unt.find("৳")+2:]
                print(unt_price)
            for b in range(1,5):
                try:
                    pack_price = driver.find_element_by_xpath('//div[@class="package-container"]['+str(b)+']').text
                    print(pack_price)
                except:
                    continue
        elif price_unt.find("ml ampoule") > 0:
            unt = driver.find_element_by_xpath('//div[@class="package-container"]').text[16:]
            length = unt.find("(")
            unt_price = unt[:length-1]
            print(unt_price)
            try:
                pack_price = driver.find_element_by_xpath('//div[@class="package-container"]//span').text[1:].replace(")","")
                print(pack_price)
            except:
                pass

        elif price_unt.find("gm tube") > 0:
            unt = driver.find_element_by_xpath('//div[@class="package-container"]').text[14:]
            unt_price = unt
            pack_price = driver.find_element_by_xpath('//div[@class="package-container"]').text
            print(unt_price)
            print(pack_price)

        elif price_unt.find("ml drop") >0:

            unt_price = price_unt[price_unt.find("৳")+2:]
            pack_price= price_unt
            print(unt_price)
            print(pack_price)

        else:
            unt = driver.find_element_by_xpath('//div[@class="package-container"]').text[14:]
            length = unt.find("(")
            if length >0:

                unt_price = unt[:length-1]
                print(unt_price)
                try:
                    pack_price = driver.find_element_by_xpath('//div[@class="package-container"]//span').text[1:].replace(")","")
                    print(pack_price)
                except:
                    pass
            else:
                unt_price = unt
                print(unt_price)
        try:
            Indications = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="indications"]//parent::div//div[@class="ac-body"]').text
            print(Indications)
        except:
            pass
        try:
            Therapeutic = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="drug_classes"]//parent::div//div[@class="ac-body"]').text
            print(Therapeutic)
        except:
            pass
        try:
            Pharmacology = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="mode_of_action"]//parent::div//div[@class="ac-body"]').text
            print(Pharmacology)
        except:
            pass
        try:

            Dosage = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="dosage"]//parent::div//div[@class="ac-body"]').text
            print(Dosage)
        except:
            pass
        try:
            Interaction = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="interaction"]//parent::div//div[@class="ac-body"]').text
            print(Interaction)
        except:
            pass
        try:
            Contraindications = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="contraindications"]//parent::div//div[@class="ac-body"]').text
            print(Contraindications)
        except:
            pass
        try:
            Side_Effects = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="side_effects"]//parent::div//div[@class="ac-body"]').text
            print(Side_Effects)
        except:
            pass
        try:
            Pregnancy = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="pregnancy_cat"]//parent::div//div[@class="ac-body"]').text
            print(Pregnancy)
        except:
            pass
        try:
            Precautions = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="precautions"]//parent::div//div[@class="ac-body"]').text
            print(Precautions)
        except:
            pass
        try:
            Populations = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="pediatric_uses"]//parent::div//div[@class="ac-body"]').text
            print(Populations)
        except:
            Overdose=driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="overdose_effects"]//parent::div//div[@class="ac-body"]').text
            print(Overdose)
        try:

            Storage = driver.find_element_by_xpath('//div[@class="generic-data-container en"]//div[@id="storage_conditions"]//parent::div//div[@class="ac-body"]').text
            print(Storage)
        except:
            pass



# https://medex.com.bd/brands/16776/acilog-100iu
# https://medex.com.bd/brands/17301/5-fu-phares-25mg