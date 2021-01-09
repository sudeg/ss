import sys
sys.path.append('../')
from PIL import Image
import templates
import icons


iPhone_11_Pro_Max_1_top_noicons_Events = Image.open("templates/iPhone_11_Pro_Max-1_top_noicons_Events.png")

iphone11_top = iPhone_11_Pro_Max_1_top_noicons_Events.copy()

iphone11_top_width, iphone11_top_height = iphone11_top.size

iPhone_11_Pro_Max_1_bottom = Image.open("templates/iPhone_11_Pro_Max-1_bottom.png")

iphone_11_bottom = iPhone_11_Pro_Max_1_bottom.copy()

iPhone_11_Pro_Max_1_bottom_width, iPhone_11_Pro_Max_1_bottom_height = iPhone_11_Pro_Max_1_bottom.size

calendar_icon_image = Image.open("icons/calendar.png")

calendar_icon = calendar_icon_image.copy()

calendar_icon = calendar_icon.resize((12, 12)) 

blank_template_for_past_image_container_image = Image.open("templates/blank_template_for_past_image_container.png")

blank_template_for_past_image_container = blank_template_for_past_image_container_image.copy()

blank_template_for_past_image_container_width, blank_template_for_past_image_container_height = blank_template_for_past_image_container.size

blank_template_for_past_information_container_image = Image.open("templates/blank_template_for_past_information_container.png")

blank_template_for_past_information_container = blank_template_for_past_information_container_image.copy()

blank_template_for_past_information_container_width, blank_template_for_past_information_container_height = blank_template_for_past_information_container.size

blank_template_for_image_container_image = Image.open("templates/blank_template_for_image_container.png")

blank_template_for_image_container = blank_template_for_image_container_image.copy()

blank_template_for_image_container_width, blank_template_for_image_container_height = blank_template_for_image_container.size

blank_template_for_information_container_image = Image.open("templates/blank_template_for_information_container.png")

blank_template_for_information_container = blank_template_for_information_container_image.copy()

blank_template_for_information_container_width, blank_template_for_information_container_height = blank_template_for_information_container.size

#general coordinates

blank_template_for_past_events_image = Image.open("templates/blank_template_for_past_events.png")

blank_template_for_past_events = blank_template_for_past_events_image.copy()

blank_template_for_past_events_width, blank_template_for_past_events_height = blank_template_for_past_events.size

blank_template_for_community_container_image = Image.open("templates/blank_template_for_community_container.png")

blank_template_for_community_container = blank_template_for_community_container_image.copy()

blank_template_for_community_container_width, blank_template_for_community_container_image_height = blank_template_for_community_container.size
