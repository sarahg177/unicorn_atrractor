from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('issue_type', 'title', 'description')


class CommentForm(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea,
        required=True)

   # class Meta:
    #    model = Comments
     #   fields = ['comment']
