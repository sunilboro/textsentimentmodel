from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def sentiment_scores(a):
    x=[input('HI, ENTER YOUR POST:'),]
    sid=SentimentIntensityAnalyzer()
    sentiment_dict=sid.polarity_scores(a)
    for a in x:
        print(a)
        boro=sid.polarity_scores(a)
    print()
    a=(boro.get('pos'))
    x=(a*100)
    happy=round(x,1)
    b=(boro.get('neu'))
    y=(b*100)
    neutral=round(y,1)
    c=(boro.get('neg'))
    z=(c*100)
    unhappy=round(z,1)
    if unhappy<30:
        m=(unhappy +(unhappy*0.1))
        sad=round(m,1)
    else:
        m=(unhappy+(unhappy*(0.5)))
        sad=round(m,1)
    print('Happy:',happy)
    print('Neutral:',neutral)
    print('Unhappy:',unhappy)
    print('Sad:',sad)
sentiment_scores("TEXT SENTIMENT MODEL")
