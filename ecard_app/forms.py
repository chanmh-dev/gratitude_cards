from django import forms
from ecard_app.models import quotes, quotes2, quotes3

class quotesForm(forms.ModelForm):
    class Meta:
        model = quotes
        fields = ['quote', 'name']
        labels = {
            'name': 'Enter your name here (姓名)',
            'quote': 'Write your gratitude here (请写下您的感恩词)'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'True', 'blank': 'False', 'label': 'Enter your name here (姓名)'},), 
            'quote': forms.Textarea(attrs={'rows': "4", 'maxlength': '250', 'class': 'form-control', 'required': 'True', 'blank': 'False',
            'label':'Write your gratitude here (请写下您的感恩词)'})
        }

    #def clean_quote(self):
        #data = self.cleaned_data['quote']
        #begin = '<p class="marquee">'
        #end = '</p> <br>'
        #data = begin + data + end
        #print('modified quote', data)
        #return data

    def clean(self):
        cleaned_data = self.cleaned_data
        begin = '<p class="marquee1">'
        end = '</p> <br>'
        cleaned_data['quote'] = begin + cleaned_data['quote'] + ' (' + cleaned_data['name'] + ')' + end
        print (cleaned_data)
        return cleaned_data        


class quotes2Form(forms.ModelForm):
    class Meta:
        model = quotes2
        fields = ['quote', 'name']
        labels = {
            'name': 'Enter your name here (姓名)',
            'quote': 'Write your gratitude here (请写下您的感恩词)'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'True', 'blank': 'False', 'label': 'Enter your name here (姓名)'},), 
            'quote': forms.Textarea(attrs={'rows': "4", 'maxlength': '250', 'class': 'form-control', 'required': 'True', 'blank': 'False',
            'label':'Write your gratitude here (请写下您的感恩词)'})
        }


    def clean(self):
        cleaned_data = self.cleaned_data
        begin = '<p class="marquee1">'
        end = '</p> <br>'
        cleaned_data['quote'] = begin + cleaned_data['quote'] + ' (' + cleaned_data['name'] + ')' + end
        print (cleaned_data)
        return cleaned_data             


class quotes3Form(forms.ModelForm):
    class Meta:
        model = quotes3
        fields = ['quote', 'name']
        labels = {
            'name': 'Enter your name here (姓名)',
            'quote': 'Write your gratitude here (请写下您的感恩词)'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'True', 'blank': 'False', 'label': 'Enter your name here (姓名)'},), 
            'quote': forms.Textarea(attrs={'rows': "4", 'maxlength': '250', 'class': 'form-control', 'required': 'True', 'blank': 'False',
            'label':'Write your gratitude here (请写下您的感恩词)'})
        }


    def clean(self):
        cleaned_data = self.cleaned_data
        begin = '<p class="marquee1">'
        end = '</p> <br>'
        cleaned_data['quote'] = begin + cleaned_data['quote'] + ' (' + cleaned_data['name'] + ')' + end
        print (cleaned_data)
        return cleaned_data   
