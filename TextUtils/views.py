# I created this file 
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    punctuations = '''!()-[]{};:'"\,|<>./?@#$%^&*_~'''
    djtext = request.GET.get('text','default');
    djremovePunc = request.GET.get('removePunc','off');
    capital = request.GET.get('capital','off');
    newlineremover = request.GET.get('newlineremover','off');
    analyzed = "";
    if djremovePunc=='on':
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char;
    elif capital == 'on':
        analyzed = analyzed + djtext.upper();
    elif newlineremover == 'on':
        for char in djtext:
            if char !='\n':
                analyzed = analyzed+char;
    else:
        analyzed="Plzz selecte the checkbox for further analysis";
    params = {'purpose':djtext,'Analyzed_text':analyzed}
    return render(request,'index.html',params);
    # return HttpResponse("Hello");
def Analyze(request):
    # punctuations = '''!()-[]{};:'"\,|<>./?@#$%^&*_~'''
    # djtext = request.GET.get('text','default');
    # djremovePunc = request.GET.get('removePunc','default');
    # if djremovePunc=='on':
    #     analyzed = "";
    #     for char in djtext:
    #         if char not in punctuations:
    #             analyzed = analyzed+char;
    # params = {'purpose':'Removed Punctuations','Analyzed_text':analyzed}
    return render(request,'Analyze.html');
