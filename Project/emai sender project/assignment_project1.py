import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "sg0175043@gmail.com"
sender_password = "wkbkkipaimdhsjal"

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_email, sender_password)
reciver_email = input("enter sender message to send email:")
Subject = "BB News International Corp US Special Offer: Request for home page advertisement on bbnewsin.com"
message = f"""/
Dear Sir,


Warm Greetings 



I take this opportunity to introduce BB News International Corp one of the World’s First Breaking Bulletin News Agency headquartered in Washington DC.



The Internet is a highly influential medium that helps consumers make decisions because of its ability to search, review, compare and buy products / services. Nowadays more than 13 crore people are using the internet in the world.

 

Why BB News International Corp Advertisement:

·   Bbnewsin.com world’s leading breaking bulletin news agency is top listed on Google for most of the business categories, due to relevant content and focussed approach.

·    Apart from the millions of customers who come directly to BB News International Corp, we also generate traffic to your site through marketing and advertising.

·  Increase engagement by posting images, call to action & hyperlinks

·  The article will rest on the platforms for a lifetime

·  PFA bbnewsin.com deck that will give you an idea of the kind of stories possible with bbnewsin.com

·  Additionally, Presenting BB News International Corp  – one of the most coveted reads which will recognize brands and industry leaders who contribute towards creating new opportunities that build the nation’s economy. This is an opportunity to have a look at the faces and stories which leave an indelible mark on the economy. PFA Jan’s feature for your reference.

·      Highest Visibility: All these ADs are installed to BB News International Corp  Website  with highest visibility and it has negligible chance of missing by Website visitors.

·      Highest Response time: Our world wide news are published  at the Website which further increases visual response time.

·      Kindly find attached advantages of BB NEWS INTERNATIONAL CORP and you may also visit our website http://bbnewsin.com for more details. 

INVESTMENT :

PRODUCT

PLATFORM

Size

UNITS

HOMEPAGE PROMOTION

NET COST* (USD)

BB News International Corp

www.bbnewsin.com

1

1

Yes

$650-$1300

2

1

Yes

$2300

3

1

Yes

$2500

4

1

Yes

$2300

5

1

Yes

$2300

6

1

Yes

$2300

 

You are requested to please include our group in your media plan.

Looking forward for a long term association

In case of any queries, please feel free to get in touch with me. Look forward to hearing from you.

Regards,

 

Shubham Garg

Sales and Advertisement

BB News International Corp

Contact Number:  +1 (202) 7738 504 |

Email:  internationaleditor@bbnewsin.com

Add:  1717 N STREET NW, SUITE 1 Washington District of Columbia 20036

"""
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = reciver_email
msg['Subject'] = Subject
body = message
msg.attach(MIMEText(body, 'plain'))

# Send the email
server.sendmail(sender_email,reciver_email, msg.as_string())
server.quit()
