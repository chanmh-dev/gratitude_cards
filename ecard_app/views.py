from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from ecard_app.models import quotes, quotes2, quotes3
from ecard_app.forms import quotesForm, quotes2Form, quotes3Form

# Create your views here.
def ecard(request):
    message1 = ''    
    message2 = ''
    message3 = ''

    submitted = False
    if request.method == 'POST':
        if 'btnform1' in request.POST:
            print('---btnform1---')
            form1 = quotesForm(request.POST)
            if form1.is_valid():
                print('---form1 valid---')
                #print('final quote', form1.cleaned_data['quote'])
                cd1 = form1.cleaned_data
                form1.save()
                # assert False
                return HttpResponseRedirect('/ecard?submitted=True')  
        elif 'btnform2' in request.POST:  
            print('---btnform2---')   
            form2 = quotes2Form(request.POST)
            if form2.is_valid():
                print('---form2 valid---')
                cd2 = form2.cleaned_data
                form2.save()
                # assert False
                return HttpResponseRedirect('/ecard?submitted=True')      
        elif 'btnform3' in request.POST:   
            print('---btnform3---')  
            form3 = quotes3Form(request.POST)
            if form3.is_valid():
                print('---form3 valid---')
                cd2 = form3.cleaned_data
                form3.save()
                # assert False
                return HttpResponseRedirect('/ecard?submitted=True')  
 
        print('empty post') 
        form1 = quotesForm()
        form2 = quotesForm()
        form3 = quotesForm()                          
    else:
        print('---GET---')
        form1 = quotesForm()
        form2 = quotesForm()
        form3 = quotesForm()
        if 'submitted' in request.GET:
            submitted = True

    all_quotes1 = quotes.objects.all().order_by('-date_time')
    #print(all_quotes1)
    if (all_quotes1):
        datetime = quotes.objects.values_list('date_time', flat=True).distinct()
        #print(datetime)
        messages = quotes.objects.values_list('quote', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message1 = message1 + message

        #print('message1', message1)

    all_quotes2 = quotes2.objects.all().order_by('-date_time')
    #print('all_quotes2', all_quotes2)
    if (all_quotes2):
        datetime = quotes2.objects.values_list('date_time', flat=True).distinct()
        print(datetime)
        messages = quotes2.objects.values_list('quote', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message2 = message2 + message

        #print('message2', message1)        


    all_quotes3 = quotes3.objects.all().order_by('-date_time')
    #print('all_quotes2', all_quotes2)
    if (all_quotes3):
        datetime = quotes3.objects.values_list('date_time', flat=True).distinct()
        print(datetime)
        messages = quotes3.objects.values_list('quote', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message3 = message3 + message

        #print('message3', message1)    

    context = {}
    text1 = """
            <div class="mqcontainer">        
            <p class="marquee">
                Happy Mother’s Day Mom! Thank you for looking after us so well, I know it’s not always easy! I love you!
                (Teo Peng Peng)
            </p>
                    
            <br>
                    
            <p class="marquee">
                母亲节快乐！——唯有一句轻轻的祝福，给所有年轻的、老迈的母亲们。(王迪)
            </p>
          </div>
        """

    text2 = """
          <div class="mqcontainer">
            <p class="marquee">
              亲爱的妈妈：您曾用您坚实的臂弯为我撑起一片蓝天，而今，我也要用我日益丰满的羽翼为您遮挡风雨。妈妈，我永远爱您！
              (刘史泰)
            </p>
                    
            <br>
                    
            <p class="marquee">
                Happy Mother’s Day to the most amazing mommy. 
                Thanks for all the diaper changes, meal times 
                (even when I throw my food on the floor), and endless outfit changes. You really are amazing!
                (John)
            </p>
          </div>
        """

    text3 = """
          <div class="mqcontainer">
            <p class="marquee">
                May all the love you gave to us come back to you a hundredfold on this special day!
                (Jenny)
            </p>
                    
            <br>
                    
            <p class="marquee">
                  妈妈，今天是母亲节我想对你说：“妈妈我爱您。”
                  （陈明明）
            </p>
          </div>
        """

    context['quote1'] = '<div class="mqcontainer">' + message1 + '</div>'
    context['quote2'] = '<div class="mqcontainer">' + message2 + '</div>'
    context['quote3'] = '<div class="mqcontainer">' + message3 + '</div>'
    context['form1'] = form1
    context['form2'] = form2
    context['form3'] = form3
    return render(request, 'ecard.html', context)

def about(request):
    return render(request, 'about.html', {})

def index(request):
    message1 = ''    
    message2 = ''
    message3 = ''

    submitted = False
    if request.method == 'POST':
        if 'btnform1' in request.POST:
            print('---btnform1---')
            form1 = quotesForm(request.POST)
            if form1.is_valid():
                print('---form1 valid---')
                #print('final quote', form1.cleaned_data['quote'])
                cd1 = form1.cleaned_data
                form1.save()
                # assert False
                return HttpResponseRedirect('/index?submitted=True')  
        elif 'btnform2' in request.POST:  
            print('---btnform2---')   
            form2 = quotes2Form(request.POST)
            if form2.is_valid():
                print('---form2 valid---')
                cd2 = form2.cleaned_data
                form2.save()
                # assert False
                return HttpResponseRedirect('/index?submitted=True')      
        elif 'btnform3' in request.POST:   
            print('---btnform3---')  
            form3 = quotes3Form(request.POST)
            if form3.is_valid():
                print('---form3 valid---')
                cd2 = form3.cleaned_data
                form3.save()
                # assert False
                return HttpResponseRedirect('/index?submitted=True')  
 
        print('empty post') 
        form1 = quotesForm()
        form2 = quotesForm()
        form3 = quotesForm()                          
    else:
        print('---GET---')
        form1 = quotesForm()
        form2 = quotesForm()
        form3 = quotesForm()
        if 'submitted' in request.GET:
            submitted = True

    all_quotes1 = quotes.objects.all().order_by('-date_time')
    #print(all_quotes1)
    if (all_quotes1):
        datetime = quotes.objects.values_list('date_time', flat=True).distinct()
        #print(datetime)
        messages = quotes.objects.values_list('quote', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message1 = message1 + message

        #print('message1', message1)

    all_quotes2 = quotes2.objects.all().order_by('-date_time')
    #print('all_quotes2', all_quotes2)
    if (all_quotes2):
        datetime = quotes2.objects.values_list('date_time', flat=True).distinct()
        print(datetime)
        messages = quotes2.objects.values_list('quote', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message2 = message2 + message

        print('message2', message1)        


    all_quotes3 = quotes3.objects.all().order_by('-date_time')
    #print('all_quotes2', all_quotes2)
    if (all_quotes3):
        datetime = quotes3.objects.values_list('date_time', flat=True).distinct()
        print(datetime)
        messages = quotes3.objects.values_list('quote', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message3 = message3 + message

        print('message3', message1)    

    context = {}
 
    context['quote1'] = '<div class="mqcontainer">' + message1 + '</div>'
    context['quote2'] = '<div class="mqcontainer">' + message2 + '</div>'
    context['quote3'] = '<div class="mqcontainer">' + message3 + '</div>'
    context['form1'] = form1
    context['form2'] = form2
    context['form3'] = form3
    
    return render(request, 'index.html', context)
 
