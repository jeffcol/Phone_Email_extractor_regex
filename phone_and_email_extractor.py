'''
Project Description.

Whenever you’re tackling a new project, it can be tempting to dive right into writing code. 
But more often than not, it’s best to take a step back and consider the bigger picture. 
I recommend first drawing up a high-level plan for what your program needs to do. 
Don’t think about the actual code yet—you can worry about that later. Right now, stick to broad strokes.

For example, your phone and email address extractor will need to do the following:

- Get the text off the clipboard.
- Find all phone numbers and email addresses in the text.
- Paste them onto the clipboard.

Now you can start thinking about how this might work in code. The code will need to do the following:

- Use the pyperclip module to copy and paste strings.
- Create two regexes, one for matching phone numbers and the other for matching email addresses.
- Find all matches, not just the first match, of both regexes.
- Neatly format the matched strings into a single string to paste.
- Display some kind of message if no matches were found in the text.
'''

#Text as example
copy_this = '''
Text:
    Contact Us

    No Starch Press, Inc.
    245 8th Street
    San Francisco, CA 94103 USA
    Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
    Fax: +1 415.863.9950

    Reach Us by Email

    General inquiries: info@nostarch.com
    Media requests: media@nostarch.com
    Academic requests: academic@nostarch.com (Further information)
    Help with your order: info@nostarch.com.co
    Reach Us on Social Media
    Twitter
    Facebook
    Instagram
    Linkedin
    Pinterest
    4258565
'''

'''
Expected:
    Copied to clipboard:
    800-420-7240
    415-863-9900
    415-863-9950
    info@nostarch.com
    media@nostarch.com
    academic@nostarch.com
    info@nostarch.com

'''

import re, pyperclip
emails = ''

#uncomment for a quick copy of the example text
#pyperclip.copy(copy_this)

phone = re.compile(r'''
( 
(\d{3})?
(\s|\.|-)?
(\d{3})
(\s|\.|-)?
(\d{4})
)
''', re.VERBOSE)


numbers = []

for number in phone.findall(pyperclip.paste()):
    numberstr = ''
    if number[1] != '':
        numberstr = '-'.join([number[1], number[3], number[5]])

    else:
        numberstr = '-'.join([number[3], number[5]])
    numbers.append(numberstr)



mail = re.compile(r'''
(
    \w+
    @
    \w+
    \.
    \w+
    (\.\w+)?
)

''', re.VERBOSE)


mailR = mail.findall(pyperclip.paste())


for i in mailR:
    emails += i[0] + '\n'


final_numbers = '\n'.join(numbers)
pyperclip.copy(final_numbers + '\n' + emails)

print('Numbers Copied to the clipboard: \n' + final_numbers)
print('Emails Copied to the clipboard: \n' + emails)


