import qrcode
import urllib
import re

# https://docs.google.com/forms/d/e/1FAIpQLSe42v3lgS8YUPTlYIkupuH56MhJzeaRakqZTjE9lRhuP1U5ow/viewform?usp=pp_url&entry.1290452009=Python+Club


# Can we write python code thbat reads in the club names from another place and creates links with the club name in them?
# Can we write python code that generates a QR code from the link?
# Can we write python code that creates a document or page that has the club name and the qr code on it that can be printed out?
# can we save the document so that people can view it or print it out?

FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSe42v3lgS8YUPTlYIkupuH56MhJzeaRakqZTjE9lRhuP1U5ow/viewform?usp=pp_url&entry.1290452009="

# read the club  list and return all the clubs in a list
def read_clubs_from_file(filename):
    with open(filename,"r",encoding = "utf8") as fp:
        clubs= []
        for  line in fp: 
            line = line.strip()
            clubs.append(line)  
        return clubs


#create a qrcode for the club and return file name
def makeqrcode(clubname):
    # qrcode.make(FORM_LINK+clubname)
    link = FORM_LINK+urllib.parse.quote_plus(clubname)

    print(link)
    qr = qrcode.QRCode(version = 1,
                   box_size = 5,
                   border = 3)

    # Adding data to the instance 'qr'
    qr.add_data(link)

    qr.make(fit = True)
    img = qr.make_image(fill_color = 'green',
                        back_color = 'gold')

    # replace any strange characters in a filename
    filename = re.sub(r"[^\w\.\-]", "", clubname) + ".png"
    img.save(filename)
    return filename

def makewebpage(clubname,qrfilename):
    filename = re.sub(r"[^\w\.\-]", "", clubname) + ".html"
    with open(filename,"w",encoding = "utf8") as fp:
        fp.write(f"<h1>{clubname}</h1>\n")
        fp.write(f'<img src="{qrfilename}" alt="{clubname}">')
    return filename

def main():
    clubs = read_clubs_from_file("clubs.txt")
    
    for clubname in clubs:
        qrfilename = makeqrcode(clubname)
        makewebpage(clubname,qrfilename)




if __name__ == "__main__":
    main()