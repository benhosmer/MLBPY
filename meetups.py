import urllib, sys
from bs4 import BeautifulSoup
import time
import Tkinter as tk

#url = "http://www.meetup.com/Melbourne-Makerspace-Florida-USA"
#html_doc = urllib.urlopen(url).read()
#print html_doc

#soup = BeautifulSoup(html_doc)
#soup = BeautifulSoup(open("meetup.html"))
#sys.exit()

def ScrollText(display_text):
    root = tk.Tk()

    #screen_width = root.winfo_screenwidth()
    screen_width = 1680 
    screen_height = root.winfo_screenheight() 

    canvas = tk.Canvas(root, height=screen_height, width=screen_width, bg="black")
    canvas.pack(fill="both", expand=1)

    font = ('courier', 48, 'bold')

    text_width = 15
    s = display_text
    charsPerScreenWidth = int(screen_width / 30) # 25px is a rough screen char width
    count = 0
    text_height = 0
    
    for char in s:
        if char == '\n':
            text_height += 55
       
    x = 20
    #y = 600
    y = screen_height
    text = canvas.create_text(x, y, anchor='nw', text=s, width=screen_width, font=font, fill='yellow')

    dx = 0
    dy = 1 # use vertical movement only

    # the pixel value depends on dx, font and length of text
    #pixels = 9000
    pixels = screen_height+text_height
    #pixels = 800 # Should be screen_height + height of text <<<<-----####        

    for p in range(pixels):
        # move text object by increments dx, dy
        # -dy = move upwards
        canvas.move(text, dx, -dy)
        canvas.update()
        # shorter delay --> faster movement
        #time.sleep(.00005)
    dy = 1
    canvas.delete(1) 
    #text = canvas.create_text(x, y, anchor='nw', text=s, width=screen_width, font=font, fill='yellow')

    #root.mainloop()
    return



def Get_Meetups(url):
    
    # Read URL
    html_doc = urllib.urlopen(url).read()
    
    # Init BeautifulSoup var
    soup = BeautifulSoup(html_doc)
    #soup = BeautifulSoup(open("meetup.html"))
    event_count = 0
    output = ""
    
    # Loop through all events and scrape data we need
    for event in soup.find_all("li", "event-item"):
        event_count += 1
        if hasattr(event.find("div", "event-title"), 'a'):
            # Grabs the event title text
            event_title = event.find("div", "event-title").a.span.text
            #print event_title        
            
            # Grabs the event date, time & location
            event_date = event.find("div", "event-meta").find("ul", "resetList").find("span", "date").text
            event_time = event.find("div", "event-meta").find("ul", "resetList").find("span", "time").text
            event_location = str(event.find("div", "event-content").find("dt", "event-venuename").a.text).strip()
            #print event_date+" "+event_time
            #print
            
            # Grabs the event description text
            if hasattr(event.find("div", "event-content").find("div", "event-desc"), 'a'):
                atag = event.find("div", "event-content").find("div", "event-desc").a
                if atag != None:
                    atag.decompose()
                
                event_desc = event.find("div", "event-content").find("div", "event-desc").text
                event_desc = event_desc.encode('ascii', 'ignore').strip()
                        
            # Grabs the event host's name
            if hasattr(event.find("p", "event-hosts"), 'a'):
                event_hosts = event.find("p", "event-hosts").a.text
            else:
                event_hosts = "Unknown"
                
            
            if event_location == "TrepHub":
                output += event_title + "\n\n"
                output += event_date+", "+event_time + "\n"
                output += event_location.strip() + "\n\n"
                output += event_desc.strip() + "\n\n"
                output += "Hosted By: " + event_hosts + "\n\n"
                output += "----------" + "\n\n"
                
                
    #print "Event count: "+str(event_count)            
    return output
        
# MAIN LOOP

Urls = []
meetup_text = ""


Urls.append("http://www.meetup.com/Melbourne-Makerspace-Florida-USA")
Urls.append("http://www.meetup.com/Coders-Hackers-Founders")

for url in Urls:
    meetup_text += Get_Meetups(url)

   
while True:
    ScrollText(meetup_text)
    #ScrollText("1 \n2 \n3 \n4 \n5 \n6 \n7 \n8 \n9 \n10 \n")

