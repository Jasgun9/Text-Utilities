# I have created this file - Jasgun
from django.http import HttpResponse #--> Imported by Jasgun Singh for http response
from django.shortcuts import render #--> Imported by Jasgun Singh for Render templates
def index(request):
    return render(request,"index.html") #--> Created by Jasgun Singh That return index.html

def analyze(request):
    djtext = request.POST.get('text', 'default')



    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
 

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    

    # if(extraspaceremover=="on"):
    #     analyzed = ""
    #     for index, char in enumerate(djtext):
    #         if not(djtext[index] == " " and djtext[index+1]==" "):
    #             analyzed = analyzed + char

    #     params = {'purpose': 'Removed Extra space', 'analyzed_text': analyzed}
    #     djtext = analyzed
 

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    if (charcounter == "on"):
        analyzed = ""
        analyzed = len(djtext)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

