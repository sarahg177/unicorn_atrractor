from django import forms
from tickets.models import Ticket, Comments


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('issue_type', 'title', 'description')


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': '10', 'cols': '5'})
    )

    class Meta:
        model = Comments
        fields = ['comment']
