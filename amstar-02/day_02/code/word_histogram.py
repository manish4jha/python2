text = '''
On a dark desert highway
Cool wind in my hair
Warm smell of colitas
Rising up through the air
Up ahead in the distance
I saw a shimmering light
My head grew heavy and my sight grew dim
I had to stop for the night
There she stood in the doorway
I heard the mission bell
And I was thinkin' to myself
'This could be heaven or this could be hell
Then she lit up a candle
And she showed me the way
There were voices down the corridor
I thought I heard them say
Welcome to the Hotel California
Such a lovely place (such a lovely place)
Such a lovely face
Plenty of room at the Hotel California
Any time of year (any time of year)
You can find it here
Her mind is Tiffany-twisted
She got the Mercedes Benz, uh
She got a lot of pretty, pretty boys
That she calls friends
How they…
'''

print(text)


# process


# split the text with respect to spaces

words = text.split()

# scan through the words and add them one by one to the dictionary

D = {}
for word in words:
    if word in D.keys():
        D[word] = D[word] + 1
    else:
        D[word] = 1

# output

print(D)
    
