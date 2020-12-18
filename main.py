from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
from time import sleep
from random import randint
from mail_client import MailClient
import requests
import datetime
import json 
import os 

class WorkBot :

    #  Function to display the exact time 

    def displayTime(self):
        now = datetime.datetime.now()
        return("["+now.strftime("%Y-%m-%d %H:%M:%S")+"] ")

    # Function to add data to JSON 

    def write_json(self,data, filename): 
        with open(filename,'w') as f: 
            json.dump(data, f, indent=4)

    # Function to write display HTML 

    def html(self,title,company,location,salary,date,link):
        html = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
<head>
<!--[if gte mso 9]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="width=device-width" name="viewport"/>
<!--[if !mso]><!-->
<meta content="IE=edge" http-equiv="X-UA-Compatible"/>
<!--<![endif]-->
<title></title>
<!--[if !mso]><!-->
<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css"/>
<link href="https://fonts.googleapis.com/css?family=Bitter" rel="stylesheet" type="text/css"/>
<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css"/>
<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css"/>
<link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet" type="text/css"/>
<link href="https://fonts.googleapis.com/css?family=Droid+Serif" rel="stylesheet" type="text/css"/>
<!--<![endif]-->
<style type="text/css">
		body {{
			margin: 0;
			padding: 0;
		}}

		table,
		td,
		tr {{
			vertical-align: top;
			border-collapse: collapse;
        }}

		* {{
			line-height: inherit;
        }}

		a[x-apple-data-detectors=true] {{
			color: inherit !important;
			text-decoration: none !important;
        }}
	</style>
<style id="media-query" type="text/css">
		@media (max-width: 520px) {{

			.block-grid,
			.col {{
				min-width: 320px !important;
				max-width: 100% !important;
				display: block !important;
        }}

			.block-grid {{
				width: 100% !important;
            }}

			.col {{
				width: 100% !important;
        }}

			.col_cont {{
				margin: 0 auto;
        }}

			img.fullwidth,
			img.fullwidthOnMobile {{
				max-width: 100% !important;
        }}

			.no-stack .col {{
				min-width: 0 !important;
				display: table-cell !important;
        }}

			.no-stack.two-up .col {{
				width: 50% !important;
        }}

			.no-stack .col.num2 {{
				width: 16.6% !important;
        }}

			.no-stack .col.num3 {{
				width: 25% !important;
        }}

			.no-stack .col.num4 {{
				width: 33% !important;
        }}

			.no-stack .col.num5 {{
				width: 41.6% !important;
        }}

			.no-stack .col.num6 {{
				width: 50% !important;
        }}

			.no-stack .col.num7 {{
				width: 58.3% !important;
        }}

			.no-stack .col.num8 {{
				width: 66.6% !important;
        }}

			.no-stack .col.num9 {{
				width: 75% !important;
        }}

			.no-stack .col.num10 {{
				width: 83.3% !important;
            }}

			.video-block {{
				max-width: none !important;
            }}

			.mobile_hide {{
				min-height: 0px;
				max-height: 0px;
				max-width: 0px;
				display: none;
				overflow: hidden;
				font-size: 0px;
            }}

			.desktop_hide {{
				display: block !important;
				max-height: none !important;
            }}
        }}
	</style>
</head>
<body class="clean-body" style="margin: 0; padding: 0; -webkit-text-size-adjust: 100%; background-color: #FFFFFF;">
<!--[if IE]><div class="ie-browser"><![endif]-->
<table bgcolor="#FFFFFF" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="table-layout: fixed; vertical-align: top; min-width: 320px; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #FFFFFF; width: 100%;" valign="top" width="100%">
<tbody>
<tr style="vertical-align: top;" valign="top">
<td style="word-break: break-word; vertical-align: top;" valign="top">
<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color:#FFFFFF"><![endif]-->
<div style="background-color:#25a8ff;">
<div class="block-grid" style="min-width: 320px; max-width: 500px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
<div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#25a8ff;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
<!--[if (mso)|(IE)]><td align="center" width="500" style="background-color:transparent;width:500px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
<div class="col num12" style="min-width: 320px; max-width: 500px; display: table-cell; vertical-align: top; width: 500px;">
<div class="col_cont" style="width:100% !important;">
<!--[if (!mso)&(!IE)]><!-->
<div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:20px; padding-bottom:20px; padding-right: 0px; padding-left: 0px;">
<!--<![endif]-->
<div style="font-size:16px;text-align:center;font-family:Arial, Helvetica Neue, Helvetica, sans-serif">
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->
<span style="color: white;font-family: Montserrat;font-size: 2.5em;">Nishpa-Bot</span>
</div>
<!--[if (!mso)&(!IE)]><!-->
</div>
<!--<![endif]-->
</div>
</div>
<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
<!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
</div>
</div>
</div>
<div style="background-color:transparent;">
<div class="block-grid" style="min-width: 320px; max-width: 500px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
<div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
<!--[if (mso)|(IE)]><td align="center" width="500" style="background-color:transparent;width:500px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:35px; padding-bottom:5px;"><![endif]-->
<div class="col num12" style="min-width: 320px; max-width: 500px; display: table-cell; vertical-align: top; width: 500px;">
<div class="col_cont" style="width:100% !important;">
<!--[if (!mso)&(!IE)]><!-->
<div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:35px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
<!--<![endif]-->
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: 'Trebuchet MS', Tahoma, sans-serif"><![endif]-->
<div style="color:#555555;font-family:'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
<div style="line-height: 1.2; font-size: 12px; color: #555555; font-family: 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif; mso-line-height-alt: 14px;">
<p style="text-align: center; line-height: 1.2; word-break: break-word; font-size: 20px; mso-line-height-alt: 24px; margin: 0;"><span style="font-size: 20px;"><strong>{title}</strong></span></p>
</div>
</div>
<!--[if mso]></td></tr></table><![endif]-->
<table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%">
<tbody>
<tr style="vertical-align: top;" valign="top">
<td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
<table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 3px solid #25A8FF; width: 45%;" valign="top" width="45%">
<tbody>
<tr style="vertical-align: top;" valign="top">
<td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
<div style="color:#555555;font-family:'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
<div style="line-height: 1.2; font-size: 12px; color: #555555; font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; mso-line-height-alt: 14px;">
<p style="text-align: center; line-height: 1.2; word-break: break-word; font-size: 16px; mso-line-height-alt: 19px; margin: 0;"><span style="font-size: 16px;"><strong>{company} </strong></span></p>
<p style="text-align: center; line-height: 1.2; word-break: break-word; mso-line-height-alt: 14px; margin: 0;"> </p>
<p style="text-align: center; line-height: 1.2; word-break: break-word; font-size: 16px; mso-line-height-alt: 19px; margin: 0;"><span style="font-size: 16px;"><strong>à {location}</strong></span></p>
<p style="text-align: center; line-height: 1.2; word-break: break-word; mso-line-height-alt: 14px; margin: 0;"> </p>
<p style="text-align: center; line-height: 1.2; word-break: break-word; font-size: 16px; mso-line-height-alt: 19px; margin: 0;"><span style="font-size: 16px;"><strong> {salary}</strong></span></p>
<p style="text-align: center; line-height: 1.2; word-break: break-word; mso-line-height-alt: 14px; margin: 0;"> </p>
<p style="text-align: center; line-height: 1.2; word-break: break-word; font-size: 16px; mso-line-height-alt: 19px; margin: 0;"><span style="font-size: 16px;color: #555;"><strong> {date}</strong></span></p>
</div>
</div>
<!--[if mso]></td></tr></table><![endif]-->
<div align="center" class="button-container" style="padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;"><tr><td style="padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="" style="height:31.5pt; width:95.25pt; v-text-anchor:middle;" arcsize="10%" stroke="false" fillcolor="#3AAEE0"><w:anchorlock/><v:textbox inset="0,0,0,0"><center style="color:#ffffff; font-family:'Trebuchet MS', Tahoma, sans-serif; font-size:12px"><![endif]-->

<a href={link}><div style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#3AAEE0;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;width:auto; width:auto;;border-top:1px solid #3AAEE0;border-right:1px solid #3AAEE0;border-bottom:1px solid #3AAEE0;border-left:1px solid #3AAEE0;padding-top:5px;padding-bottom:5px;font-family:'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:20px;padding-right:20px;font-size:12px;display:inline-block;"><span style="line-height: 24px; word-break: break-word;"><strong>Apply</strong></span></span></div></a>
<!--[if mso]></center></v:textbox></v:roundrect></td></tr></table><![endif]-->
</div>
<!--[if (!mso)&(!IE)]><!-->
</div>
<!--<![endif]-->
</div>
</div>
<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
<!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
</div>
</div>
</div>
<div style="background-color:transparent;">
<div class="block-grid" style="min-width: 320px; max-width: 500px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; background-color: transparent;">
<div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
<!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
<!--[if (mso)|(IE)]><td align="center" width="500" style="background-color:transparent;width:500px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
<div class="col num12" style="min-width: 320px; max-width: 500px; display: table-cell; vertical-align: top; width: 500px;">
<div class="col_cont" style="width:100% !important;">
<!--[if (!mso)&(!IE)]><!-->
<div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
<!--<![endif]-->
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
<div style="color:#555555;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
<div style="line-height: 1.2; font-size: 12px; color: #555555; font-family: Arial, Helvetica Neue, Helvetica, sans-serif; mso-line-height-alt: 14px;">
<p style="font-size: 14px; line-height: 1.2; word-break: break-word; text-align: center; mso-line-height-alt: 17px; margin: 0;"><span style="color: #808080;">Don't forget to clear JSON every two month </span>😉</p>
</div>
</div>
<!--[if mso]></td></tr></table><![endif]-->
<!--[if (!mso)&(!IE)]><!-->
</div>
<!--<![endif]-->
</div>
</div>
<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
<!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
</div>
</div>
</div>
<!--[if (mso)|(IE)]></td></tr></table><![endif]-->
</td>
</tr>
</tbody>
</table>
<!--[if (IE)]></div><![endif]-->
</body>
</html>"""

        return html

    
    # Running the main script

    def run(self):   

        running = True

        while running : 

            ua = UserAgent().random

            # Define webdriver options 

            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('window-size=1400,600')
            options.add_argument("user-agent="+str(ua))

            #  Launching webdriver

            print(self.displayTime()+"Launching ...")

            self.driver = webdriver.Chrome(options=options)

            self.url = the url you want to scrape
    
            self.driver.get(self.url)

            response = self.driver.page_source 

            page = BeautifulSoup(response, 'html.parser')

            annonces = page.select('.jobsearch-SerpJobCard.unifiedRow.row.result.clickcard')

            mail = MailClient(mail adress of sender, password of sender)


            data = []

            new_offers = None

            same = False

            i = 0

            # Setting variables 

            title = []
            company = []
            location = []
            salary = []
            date = []
            link = []

            for annonce in annonces :

                    # Job title

                    titleA = annonce.select('.jobtitle')
                    titleA = titleA[0].text.strip()
                    title.append(titleA)

                    # Company

                    companyA = annonce.select('.company')
                    companyA = companyA[0].text.strip()
                    company.append(companyA)

                    # Location

                    locationA = annonce.select('.location')
                    locationA = locationA[0].text.strip()
                    location.append(locationA)

                    # Salary

                    salaryA = annonce.select('span.salaryText')

                    if(len(salaryA)==0):

                        salaryA = None

                    else :

                        salaryA = salaryA[0].text.strip()

                    salary.append(salaryA)

                    # Date

                    dateA = annonce.select('span.date')

                    dateA = dateA[0].text.strip()

                    date.append(dateA)

                    # Link 

                    linkA = annonce.select('.title a')
                    
                    linkA = linkA[0].get('href')

                    linkA = f'https://fr.indeed.com{linkA}'
                    
                    link.append(linkA)

            # If json file doesn't exist

            if os.path.isfile('job_offers.json') == False:



                for annonce in annonces :

                    # Send mail

                    subject = f'[NOUVELLE OFFRE] {title[i]}' 

                    body = f'Poste : {title[i]}\nEntreprise : {company[i]}\nLieu : {location[i]}\nSalaire : {salary[i]}\nDate : {date[i]}\nLien : {link[i]}\nDon\'t forget to clear JSON every 2 months'


                    if salary[i] == None :

                        html = self.html(title[i],company[i],location[i],'Salaire à déterminer',date[i],link[i])
                    
                    else :

                        html = self.html(title[i],company[i],location[i],salary[i],date[i],link[i])

                    mail.send(subject,body,html,sender mail adress,receiver mail adress)
                    
                    

                    data.append({
                        'title' : title[i],
                        'company' :  company[i],
                        'location' : location[i],
                        'salary' : salary[i],
                        'date' : date[i],
                        'link' : link[i]
                    })

                    i+=1
                    
                    
                
                self.write_json(data,'job_offers.json')

            # If json file exists

            else :

                with open('job_offers.json') as json_file:

                        existing_offers = json.load(json_file)
                        copycat = existing_offers
                

                for annonce in annonces :

                    

                    for offer in existing_offers :


                        # Check if we already stored this offer
                        

                        if offer['title'] == title[i] and offer['company'] == company[i] and offer['location'] == location[i] and offer['salary'] == salary[i] and offer['link'] == link[i]     :

                            same = True

                        


                    # Send mail


                    if same==False  :   

                        subject = f'[NOUVELLE OFFRE] {title[i]}' 

                        body = f'Poste : {title[i]}\nEntreprise : {company[i]}\nLieu : {location[i]}\nSalaire : {salary[i]}\nDate : {date[i]}\nLien : {link[i]}\nDon\'t forget to clear JSON every 2 months'


                        if salary[i] == None :

                            html = self.html(title[i],company[i],location[i],'Salaire à déterminer',date[i],link[i])
                        
                        else :

                            html = self.html(title[i],company[i],location[i],salary[i],date[i],link[i])

                        mail.send(subject,body,html,sender mail adress, receiver mail adress)  

                        new_offers = {
                            'title' : title[i],
                            'company' :  company[i],
                            'location' : location[i],
                            'salary' : salary[i],
                            'date' : date[i],
                            'link' : link[i]
                        }
                    
                        copycat.append(new_offers)

                    i+=1
                    same = False

                    

                

                self.write_json(copycat,'job_offers.json')
                
                print(self.displayTime()+"Successful Run ...")

                print(self.displayTime()+"Closing the browser ")

                self.driver.close()

                print(self.displayTime()+"Sleeping ... ")

                sleep(randint(1800,2100))

wb = WorkBot()
wb.run()              


            


                

    



