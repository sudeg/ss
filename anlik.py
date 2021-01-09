import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

import json
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import textwrap 


resim = Image.open("/Users/anilyavuz6176gmail.com/Desktop/ss/templates/community_resim_template.png")

a = resim.copy()

b = resim.copy()

c = resim.copy()

d = resim.copy()

e = resim.copy()

f = resim.copy()

a.resize((233,152))

a.save("/Users/anilyavuz6176gmail.com/Desktop/ss/templates/blank_template_for_past_image_container.png")

b.resize((233,152))

b.save("/Users/anilyavuz6176gmail.com/Desktop/ss/templates/blank_template_for_past_information_container.png")

c.resize((461, 186))

c.save("/Users/anilyavuz6176gmail.com/Desktop/ss/templates/blank_template_for_image_container.png")

d.resize((461, 186))

d.save("/Users/anilyavuz6176gmail.com/Desktop/ss/templates/blank_template_for_information_container.png")

e.resize((233, 304))

e.save("/Users/anilyavuz6176gmail.com/Desktop/ss/templates/blank_template_for_past_events.png")

f.resize((461, 372))

f.save("/Users/anilyavuz6176gmail.com/Desktop/ss/templates/blank_template_for_community_container.png")