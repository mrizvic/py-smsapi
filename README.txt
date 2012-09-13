ABOUT:

I wrote that for my personal use with SMS API provider in Slovenia - http://www.smsapi.si/

It reads a single line of text followed by another line that should contain GSM number of recipient.
After user confirms his/her message by typing 'yes' the HTTP request is generated and executed against SMS API provider.

USAGE:

$ ./smsapi.py
Type your message in one line:
hello world
Enter recipient's GSM number:
aaabbbccc	<== replace aaabbbccc with 9 digit gsm number
Send? (yes/NO)
yes
sending...
<HTTP response dump from server>

DISCLAIMER:

I am not responsible for any damage that can be done by using this code.
