import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

import json
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import textwrap 
import pandas as pd
import json
from matplotlib import pyplot as plt        # Just for visualization
import requests


# global parameters

event_image = Image.open("/Users/anilyavuz6176gmail.com/Desktop/ss/images/cur1.png")

theme_color = "006000"

# title = "anilili"

# location = "sudedededede"
 
# date = "datetete"

#globals

iPhone11_top_home_image = Image.open("/Users/anilyavuz6176gmail.com/Desktop/ss/templates/iPhone_11_Pro_Max-1_top_noicons_Home.png")

iphone_11_top_home = iPhone11_top_home_image.copy()

iPhone_11_Pro_Max_1_top_noicons_Events = Image.open("templates/iPhone_11_Pro_Max-1_top_noicons_Events.png")

iphone11_top_events = iPhone_11_Pro_Max_1_top_noicons_Events.copy()

iPhone_11_Pro_Max_1_bottom = Image.open("templates/iPhone_11_Pro_Max-1_bottom.png")

iphone_11_bottom = iPhone_11_Pro_Max_1_bottom.copy()

iPhone_11_Pro_Max_1_bottom_width, iPhone_11_Pro_Max_1_bottom_height = iPhone_11_Pro_Max_1_bottom.size

iPhone_8_Plus_1_top_Home = Image.open("/Users/anilyavuz6176gmail.com/Desktop/ss/templates/android_ss1_top_Home_noicons.png")

iphone8_top_home = iPhone_8_Plus_1_top_Home.copy()

iPhone_8_Plus_1_top_Events = Image.open("/Users/anilyavuz6176gmail.com/Desktop/ss/templates/iPhone_8_Plus-1_top_Events.png")

iphone8_top_events = iPhone_8_Plus_1_top_Events.copy()

iPhone_8_Plus_1_bottom = Image.open("/Users/anilyavuz6176gmail.com/Desktop/ss/templates/iPhone_8_Plus-1_bottom.png")

iphone8_bottom = iPhone_8_Plus_1_bottom.copy()

iphone8_bottom_width, iphone8_bottom_height = iphone8_bottom.size


android_top_events_noicons = Image.open("/Users/anilyavuz6176gmail.com/Desktop/ss/templates/android_ss1_top_Events_noicons.png")

android_top_events = android_top_events_noicons.copy()

android_top_home_noicons = Image.open("/Users/anilyavuz6176gmail.com/Desktop/ss/templates/android_ss1_top_Home_noicons.png")

android_top_home = android_top_home_noicons.copy()

android_bottom_image = Image.open("/Users/anilyavuz6176gmail.com/Desktop/ss/templates/android_ss1_bottom.png")

android_bottom = android_bottom_image.copy()

android_bottom_width, android_bottom_height = android_bottom.size

calendar_icon_image = Image.open("icons/calendar.png")

calendar_icon = calendar_icon_image.copy()

calendar_icon = calendar_icon.resize((18, 17)) 

#fonts 

sfpro_medium = ImageFont.truetype("/Users/anilyavuz6176gmail.com/Desktop/ss/fonts/FontsFree-Net-SFProDisplay-Medium.ttf",16)

sfpro_Semibold_big = ImageFont.truetype("/Users/anilyavuz6176gmail.com/Desktop/ss/fonts/FontsFree-Net-SFProDisplay-Semibold.ttf",24)

sfpro_Semibold_small = ImageFont.truetype("/Users/anilyavuz6176gmail.com/Desktop/ss/fonts/FontsFree-Net-SFProDisplay-Semibold.ttf",18)

sfpro_regular = ImageFont.truetype("/Users/anilyavuz6176gmail.com/Desktop/ss/fonts/FontsFree-Net-SFProDisplay-Regular.ttf",16)

roboto_medium = ImageFont.truetype("/Users/anilyavuz6176gmail.com/Desktop/ss/fonts/Roboto-Medium.ttf",16)

roboto_bold_big = ImageFont.truetype("/Users/anilyavuz6176gmail.com/Desktop/ss/fonts/Roboto-Bold.ttf",24)

roboto_bold_small = ImageFont.truetype("/Users/anilyavuz6176gmail.com/Desktop/ss/fonts/Roboto-Bold.ttf",18)

roboto_regular = ImageFont.truetype("/Users/anilyavuz6176gmail.com/Desktop/ss/fonts/Roboto-Regular.ttf",16)

# get json data

source = open('example2.json',)
data = json.load(source)

def add_corners (im, rad):
    circle = Image.new ('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw (circle)
    draw.ellipse ((0, 0, rad * 2, rad * 2), fill = 255)
    alpha = Image.new ('L', im.size, 255)
    w, h = im.size
    alpha.paste (circle.crop ((0, 0, rad, rad)), (0, 0))
    alpha.paste (circle.crop ((0, rad, rad, rad * 2)), (0, h-rad))
    alpha.paste (circle.crop ((rad, 0, rad * 2, rad)), (w-rad, 0))
    alpha.paste (circle.crop ((rad, rad, rad * 2, rad * 2)), (w-rad, h-rad))
    im.putalpha (alpha)
    return im

def hex_to_rgb(value):

    lv = len(value)

    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

def getTopImage(phone_type,theme_color):

    #changing top image with theme color

    theme_color_rgb = hex_to_rgb(theme_color)

    if phone_type == "iPhone11_container":

        image = iphone_11_top_home
    
    elif phone_type == "iPhone11_events":

        image = iphone11_top_events

    elif phone_type == "iphone8_events":

        image = iphone8_top_events

    elif phone_type == "iphone8_container":

        image = iphone8_top_home

    elif phone_type == "android_events": 

        image = android_top_events

    elif phone_type == "android_container":

        image = android_top_home

    elif phone_type == "android_events":

        image = android_top_events

    width, height = image.size

    for x in range(width): 
        for y in range(height):
            r,g,b,a = image.getpixel((x,y))
            if a > 135:
              image.putpixel((x,y), theme_color_rgb)

    return image

def getImagePart(image, type):

    im = Image.open(requests.get(image, stream=True).raw)

    if type == "community" or type == "current":

        dst = Image.new('RGB', (461,186),(255,255,255))

        dst_width, dst_height = dst.size

        im.thumbnail((dst_width*(1.4),dst_height*(1.4)))
        im.resize((461,186))

    elif type == "past":

        dst = Image.new('RGB', (233,126),(255,255,255))
        dst_width, dst_height = dst.size
   
        im.thumbnail((dst_width*(1.4),dst_height*(1.4)))
        im.resize((233,126))

    dst.paste(im,(0,0))

    return dst

def getInformationPart(information, type, phone):

    if phone == "iPhone11" or phone == "iPhone8" : 

        medium = sfpro_medium
        bold_small = sfpro_Semibold_small
        regular = sfpro_regular

    elif phone == "android" : 

        medium = roboto_medium
        bold_small = roboto_bold_small
        regular = roboto_regular
 
    if type == "community" or type == "current":

        dst = Image.new('RGB', (461,124),(255,255,255))

    elif type == "past":

        dst = Image.new('RGB', (233,152),(255,255,255))

    editable_container = ImageDraw.Draw(dst)

    if type == "community" : 

        editable_container.text((21, 16), information["communityName"], (47,47,47), font = bold_small)

    else :

        editable_container.text((21, 16), information["eventName"], (47,47,47), font = bold_small)

        if "eventType" in information:

            editable_container.text((21,46), information["eventType"], (47,47,47), font = regular)

            editable_container.text((65, 46), information["eventLocation"], (47,47,47), font = regular)

        else :

            editable_container.text((21,46), information["eventLocation"], (47,47,47), font = regular)

        dst.paste(calendar_icon, (22, 80), calendar_icon)
        editable_container.text((49, 80), information["eventDate"], (47,47,47), font = medium)

    return dst

def createContainer(type, image, information):

    if type == "community" or type == "current":

        dst = Image.new('RGB', (461,310),(255,255,255))

    elif type == "past":

        dst = Image.new('RGB', (233,279),(255,255,255))
    
    dst.paste(image, (0, 0))
    dst.paste(information, (0, image.height))
    
    dst = add_corners(dst, 8)

    dst_width, dst_height = dst.size

    for x in range(dst_width): 
        for y in range(dst_height):
            r,g,b,a = dst.getpixel((x,y))
            if a == 0:
                dst.putpixel((x,y), (252,252,252))

    return dst

def insertHeaderText(firstContainer, type, width, height, phone): 


    if phone == "iPhone11" or phone == "iPhone8" : 

        bold_big =  sfpro_Semibold_big

    elif phone == "android" : 

        bold_big =  roboto_bold_big
 
    editable_container = ImageDraw.Draw(firstContainer)

    if type == "past" :

        title = "Past Events"

        editable_container.text((width, height), title, (47,47,47), font = bold_big)

    elif type == "current" : 

        title = "Current & Upcoming Events"

        editable_container.text((width, height), title, (47,47,47), font = bold_big)

    elif type == "community" :

        title = "Community"

        editable_container.text((width, height), title, (47,47,47), font = bold_big)

    return firstContainer

def createScreenshot(phone):

    if phone == "iPhone11":

        whole_template = iphone_11_bottom

    elif phone == "android":

        whole_template = android_bottom

    elif phone == "iPhone8":

        whole_template = iphone8_bottom
 

    if "communities" in data: 

        if phone == "iPhone11":

            phone_type = "iPhone11_container"

            top = getTopImage(phone_type,theme_color)

            whole_template.paste(top, (0,0), top)

            whole_template.thumbnail((552, 1194))

            for_bottom = whole_template.crop((0, 1083, 552, 1194))


        elif phone == "android":

            phone_type = "android_container"

            top = getTopImage(phone_type,theme_color)

            whole_template.paste(top, (0,0), top)
            
            whole_template.thumbnail((529, 976))

            for_bottom = whole_template.crop((0, 808, 529, 940))


        # elif phone == "iPhone8":

        #     phone_type = "iphone8_container"

        #     top = getTopImage(phone_type,theme_color)
    
        #     whole_template.paste(top, (0,0), top)

        #     for_bottom = whole_template.crop((0, 1082, 552, 1194))

        #     whole_template.thumbnail((552, 1194))

        type = "community"


        whole_template = insertHeaderText(whole_template, type, 32, 278, phone)

        start_x = 32
        start_y = 320

        for i in range(0, len(data["communities"])):

            image_part = getImagePart(data["communities"][i]["coverImage"], type)

            information_part = getInformationPart(data["communities"][i], type, phone)

            communityContainer = createContainer(type, image_part, information_part)

            whole_template.paste(communityContainer, (start_x, start_y))

            start_x = start_x + 482

        if "events" in data: 

            count = 0 

            past_count = 0

            for i in range(0, len(data["events"])):

                if data["events"][i]["eventStatus"] == "current" : 

                    count += 1

            for i in range(0, len(data["events"])):

                if data["events"][i]["eventStatus"] == "past" : 

                    past_count += 1

            if count > 0 : 

                secondType = "current"

                whole_template = insertHeaderText(whole_template, secondType, 32, 662, phone)

                second_start_x = 32
                second_start_y = 706

                for i in range(0, len(data["events"])):
                    
                    second_image_part = getImagePart(data["events"][i]["coverImage"], secondType)

                    second_information_part = getInformationPart(data["events"][i], secondType, phone)

                    currentContainer = createContainer(secondType, second_image_part, second_information_part)

                    whole_template.paste(currentContainer, (second_start_x, second_start_y))

                    second_start_x = second_start_x + 482

            elif count == 0 and past_count > 0 : 

                thirdType = "past"

                whole_template = insertHeaderText(whole_template, thirdType, 32, 662, phone)

                left_x = 32
                right_x = 286
                left_y = 706
                right_y = 706

                for i in range(0, len(data["events"])):
                    

                        third_image_part = getImagePart(data["events"][i]["coverImage"], thirdType)

                        third_information_part = getInformationPart(data["events"][i], thirdType, phone)

                        currentContainer = createContainer(thirdType, third_image_part, third_information_part)

                        if i % 2 == 0 : 

                            whole_template.paste(currentContainer, (left_x, left_y))

                            left_y = left_y + 300


                        else : 

                             whole_template.paste(currentContainer, (right_x, right_y))

                             right_y = right_y + 300

    else: 


        if phone == "iPhone11":

            phone_type = "iPhone11_events"

            top = getTopImage(phone_type,theme_color)

            whole_template.paste(top, (0,0), top)

            whole_template.thumbnail((552, 1194))

            for_bottom = whole_template.crop((0, 1083, 552, 1194))


        elif phone == "android":

            phone_type = "android_events"

            top = getTopImage(phone_type,theme_color)

            whole_template.paste(top, (0,0), top)
            
            whole_template.thumbnail((529, 976))

            for_bottom = whole_template.crop((0, 808, 529, 940))

        # elif phone == "iPhone8":

        #     phone_type = "iphone8_events"

        #     top = getTopImage(phone_type,theme_color)
    
        #     whole_template.paste(top, (0,0), top)

        #     for_bottom = whole_template.crop((0, 1082, 552, 1194))

        #     whole_template.thumbnail((552, 1194))

        count = 0 

        past_count = 0

        for i in range(0, len(data["events"])):

            if data["events"][i]["eventStatus"] == "current" : 

                count += 1

        for i in range(0, len(data["events"])):

            if data["events"][i]["eventStatus"] == "past" : 

                past_count += 1
        
        if count > 0 : 

            start_x = 32
            start_y = 320

            left_x = 32
            right_x = 286
            left_y = 706
            right_y = 706

            type = "current"    

            secondType = "past"        

            whole_template = insertHeaderText(whole_template, type, 32, 278, phone)

            if past_count > 0 : 

                whole_template = insertHeaderText(whole_template, secondType, 32, 662, pjone)

            for i in range(0, len(data["events"])):

                if data["events"][i]["eventStatus"] == "current":
                
                    image_part = getImagePart(data["events"][i]["coverImage"], type)

                    information_part = getInformationPart(data["events"][i], type, phone)

                    currentContainer = createContainer(type, image_part, information_part)

                    whole_template.paste(currentContainer, (start_x, start_y))

                    start_x = start_x + 482

                if data["events"][i]["eventStatus"] == "past":

                            second_image_part = getImagePart(data["events"][i]["coverImage"], secondType)

                            second_information_part = getInformationPart(data["events"][i], secondType, phone)

                            second_currentContainer = createContainer(secondType, second_image_part, second_information_part)

                            if i % 2 == 0 : 

                                whole_template.paste(second_currentContainer, (left_x, left_y))

                                left_y = left_y + 300


                            else : 

                                whole_template.paste(second_currentContainer, (right_x, right_y))

                                right_y = right_y + 300 

                if past_count > 2 : 

                    whole_template.paste(for_bottom,(0, 1082))
        
        else : 

            type = "past"

            whole_template = insertHeaderText(whole_template, type, 32, 278, phone)

            left_x = 32
            right_x = 286
            left_y = 322
            right_y = 322

            for i in range(0, len(data["events"])):

                image_part = getImagePart(data["events"][i]["coverImage"], type)

                information_part = getInformationPart(data["events"][i], type, phone)

                currentContainer = createContainer(type, image_part, information_part)

                if i % 2 == 0 : 

                    whole_template.paste(currentContainer, (left_x, left_y))

                    left_y = left_y + 300


                else : 

                        whole_template.paste(currentContainer, (right_x, right_y))

                        right_y = right_y + 300


    if phone == "iPhone11": 

        whole_template.paste(for_bottom,(0,1082), for_bottom)   

    elif phone == "android" : 

        whole_template.paste(for_bottom,(0,808), for_bottom)   


    # elif phone == "iPhone8" : 
    #     for_bottom = whole_template.crop((0, 1082, 552, 1194))
    #     whole_template.paste(for_bottom,(0,1082), for_bottom)   

    return whole_template

def createAllScreenshots():

    iPhone11 = "iPhone11"
    createScreenshot(iPhone11).save("/Users/anilyavuz6176gmail.com/Desktop/ss/tests/iPhone11.png")
    # iPhone8 = "iPhone8"
    # createScreenshot(iPhone8).save("/Users/anilyavuz6176gmail.com/Desktop/ss/tests/iPhone8.png")
    android = "android"
    createScreenshot(android).save("/Users/anilyavuz6176gmail.com/Desktop/ss/tests/android.png")

    
createAllScreenshots()