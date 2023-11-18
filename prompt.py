wikipedia_template = """Question: {query}

Please only use wikipedia when searching for the answer.




When given a query you must generate a wikipedia article based on the query given;
You must oranization your article into sections just like in wikipedia
The structure is open ended however you must write this article in markdown;
Also you must have a reference section at the end with a list of all your refernces;
If you are unsure about the exact person the user is refering to please ask questions;

For the sake of clarity please add new lines between your inital output and the
generated wikipedia article


If there are many pages for a similar person or entity please as
the user to specify which one they are talking about before geenrating the article

Please make sure to include in-line citations

for example:
fact_1 [source_1]
fact_2 [source_2, source_3]
Answer: 
"""

# general_internet_template = """Question: {query}

# Please only use {website_list} when searching for the answer.


# When given a query you must generate a wikipedia article based on the query given;
# You must oranization your article into sections just like in wikipedia
# The structure is open ended however you must write this article in markdown;
# Also you must have a reference section at the end with a list of all your refernces;
# If you are unsure about the exact person the user is refering to please ask questions;

# For the sake of clarity please add new lines between your inital output and the
# generated wikipedia article


# If there are many pages for a similar person or entity please as
# the user to specify which one they are talking about before geenrating the article

# Please make sure to include in-line citations

# for example:
# fact_1 [source_1]
# fact_2 [source_2, source_3]
# Answer: 
# """


general_internet_template = """Question: {query}

Use any website so needed to help the user.



When given a query you must generate a wikipedia article based on the query given;
You must oranization your article into sections just like in wikipedia
The structure is open ended however you must write this article in markdown;
Also you must have a reference section at the end with a list of all your refernces;
If you are unsure about the exact person the user is refering to please ask questions;

For the sake of clarity please add new lines between your inital output and the
generated wikipedia article


If there are many pages for a similar person or entity please as
the user to specify which one they are talking about before geenrating the article

Please make sure to include in-line citations

for example:
fact_1 [source_1]
fact_2 [source_2, source_3]
Answer: 
"""