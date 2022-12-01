from django import forms
from .models import Event, Comment
from model_utils import Choices
from ckeditor.fields import RichTextFormField

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
    
    # overriding default form setting and adding bootstrap class
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'placeholder': 'Enter name','class':'form-control'}
        self.fields['email'].widget.attrs = {'placeholder': 'Enter email', 'class':'form-control'}
        self.fields['body'].widget.attrs = {'placeholder': 'Comment here...', 'class':'form-control', 'rows':'5'}

class EventPostForm(forms.ModelForm):
    event_body = RichTextFormField()
    class Meta:
        model = Event
        fields = ('event_title', 'event_slug', 'event_body', 'event_featured_image','event_start_date','event_end_date','event_start_time','event_end_time','event_venue','event_address','event_city','event_state','event_country','event_ticket_option','event_onlinepayment_option','event_event_images','event_organizer_name','event_sponsors','event_event_type','event_event_topic','event_listing_privacy','event_remaining_tickets','status','tags')

        EVENT_TICKET_OPTION = [
    ('free', 'Free'),
    ('Paid', 'paid'),
    ('donation', 'Donation'),
    ]
        EVENT_TOPIC= [
    ('Class, Training, Workshop, Seminar'),
    ('Concert or Performance'),
    ('Conference'),
    ('Convention'),
    ('Festival or Fair'),
],


          

        widgets = {
            'event_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Event'}),
            'event_slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            #'event_body': forms.Textarea(attrs={'class':'form-control', 'rows':'6'}),
            'event_start_date': forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'event_end_date': forms.TextInput(attrs={'class':'form-control datetimepicker'}),
            'event_start_time': forms.TextInput(attrs={'class':'form-control datetimepicker', 'data-options': '{"enableTime":true,"noCalendar":true,"dateFormat":"H:i","disableMobile":true}'}),
            'event_end_time': forms.TextInput(attrs={'class':'form-control datetimepicker', 'data-options': '{"enableTime":true,"noCalendar":true,"dateFormat":"H:i","disableMobile":true}'}),
            'event_venue': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Place/Hall Name'}),
            'event_address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address Of Event'}),
            'event_city': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Event City'}),
            'event_state': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Event State'}),
            'event_country': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Event Country'}),
            'event_ticket_option': forms.Select(choices=EVENT_TICKET_OPTION,attrs={'class':'form-control'}),
            'event_onlinepayment_option': forms.TextInput(attrs={'class':'form-control'}),
            'event_organizer_name': forms.TextInput(attrs={'class':'form-control'}),
            'event_sponsors': forms.TextInput(attrs={'class':'form-control'}),
            
            'event_event_type': forms.TextInput(attrs={'class':'form-control','placeholder':'Workshop, Smeinar ,Fair Festival'}),
            'event_event_topic': forms.TextInput(attrs={'class':'form-control','placeholder':'Bussiness, Charity ,Education, Culture'}),
            'event_listing_privacy': forms.TextInput(attrs={'class':'form-control','placeholder':'Public, Private '}),
            'event_remaining_tickets': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.TextInput(attrs={'class':'form-control'}),
            'tags': forms.TextInput(attrs={'class':'form-control', 'placeholder':'#seminar #event'}),
        }        