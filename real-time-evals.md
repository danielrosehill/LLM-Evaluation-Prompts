# Prompts for evaluating augmented retrieval capabilities

## Example prompts to assess recent news retrieval 

At the time of writing, and because of the type of thing that interests me, I have been using the following prompts - or varieties of them - for assessing wheher an LLM has workable *recent* news retrieval capabilities:

>The International Criminal Court (ICC) recently issued arrest warrants against two Israeli statesmen. What date was that ruling issued on and which statesmen were targeted?

Or:

>What was the official reaction of Ireland to the ceasefire announced in late November between Israel and Hizbullah? Can you provide a detailed quote from the head of state?

## Example prompts to assess real time data retrieval capabilities

If you're interested in assessing specific real time data of interest, you can prompt in any number of ways:

>What is the current trading price of Tesla?

(Verify against a financial API / manual search)

>What is the current temperature in New York City?

(Verify against a weather API / manual search)

>What is the current altitude and location of flight {flight-number}?

(Verify against ADS-B data source)