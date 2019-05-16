run `pip install -r "requirements.txt"`

run `python question_x.py` where x is a, b or c to execute the code relating to the assoctiated question

All inputs will be prompted, nothing needs to be entered as `*args`


Thoughts on question C
--

My code simply relies on google to return the five mosts relevant results, there is no handpicking of websites.
Choosing what content of the website is most relevant still feels too arbitrary to me.

I decided to select the paragraph with the densest concentration of queried words in it. This should return the "most relevant" 
paragraph to the user. Doing this, I found myself getting paragraphs that are one or two words long, making it a poor summary of the website.
I decided to omit all paragraphs under 10 words, which is quite arbitrary, but it can now select more relevant paragraphs.

I also do not have any code ranking the importance of words, meaning that "for" would be as relevant as "keystone".
There could be a list of omitted words as well, but some queries would be affected, such as "python for loop tutorial".
To remedy this true NLP would have to be implemented.

Selection of what a paragraph is can also be improved, I chose to separate them at every "\n". I tried separating them by
tags, however this resulted in getting enormous summaries which included footers of webpages, and were terrible summaries.
