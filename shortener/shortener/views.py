from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Link, Clicked
from django.db.models import Count
import random
import string
import datetime
from collections import Counter

def index(request):
    return render(request, "index.html")

def all_links(request):
    allLinks = Link.objects.order_by('url')
    d = {"links": allLinks}
    return render(request, "alllinks.html", d)

def redirectShortened(request, shortURL):

    try:
        link = Link.objects.get(shortened = shortURL)
        link.count += 1
        link.save()
        newClick = Clicked(link = link)
        newClick.save()
        return redirect("https://www." + link.url, permanent=True)
    except:
        d = {"shortURL" : shortURL}
        return render(request, "nonexistent.html", d)


def shorten(request, longURL=None):
    """
    An endpoint that receives a URL and returns a new shortened URL
    """

    if longURL is None or len(longURL) <= 1:
        return render(request, "shorten.html")

    while True:
        #create code of size 8
        newShortCode = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        try:
            isSameCode = Link.objects.get(shortened = newShortCode)
        except:
            #there was an error, meaning no links existed with the shortened link equal
            #to the value of newShortCode
            newLink = Link(url=longURL, shortened = newShortCode)
            newLink.save()
            d = {"longURL" : longURL, "shortURL" : newShortCode, "id" : newLink.id}
            return render(request, "shortenCompleted.html", d)


def recent(request):
    """
    An endpoint to retrieve the last 100 shortened URLs
    """
    mostRecent = Link.objects.order_by('-timeCreated')
    print(mostRecent)
    d = {"recent" : mostRecent}
    return render(request, "recent.html", d)


def top(request):
    """
    An endpoint to retrieve the top 10 most popular shortened domains in the past month
    """
    today = datetime.date.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)

    recentLinks = []
    recentClicks = Clicked.objects.filter(clickAt__range=(lastMonth, today)).select_related('link')
    for c in Clicked.objects.filter(clickAt__range=(lastMonth, today)).select_related('link'):
        recentLinks.append(c.link)

    ctr = Counter(recentLinks)
    topLinks = ctr.most_common(10)
    d = {"top" : topLinks}
    return render(request, "top.html", d)


def count(request, shortURL = None):
    """
    An endpoint to retrieve the number of times a shortened URL has been visited.
    """
    if shortURL is None or len(shortURL) <= 1:
        return render(request, "count.html")
        
    hitCount = Link.objects.get(shortened = shortURL).count
    d = {"shortURL": shortURL, "count" : hitCount}
    return render(request, "countCompleted.html", d)
