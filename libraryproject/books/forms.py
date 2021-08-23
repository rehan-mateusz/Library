from django import forms

from . import models


class BookForm(forms.ModelForm):

    class Meta():
        model = models.Book
        fields = '__all__'

    def clean(self):
        super(BookForm, self).clean()
        isbn_13 = self.cleaned_data['isbn_13']
        if isbn_13 is not None:
            if not isbn_13.isnumeric():
                self.add_error('isbn_13', 'Only numbers allowed!')


class GoogleForm(forms.Form):
    intitle = forms.CharField(required=False, label='Title contains:')
    inauthor = forms.CharField(required=False, label='Author contains:')
    inpublisher = forms.CharField(required=False, label='Publisher contains:')
    subject = forms.CharField(required=False, label='Categories contain:')
    isbn = forms.CharField(required=False, label='ISBN containts:')
    lccn = forms.CharField(required=False,
                           label='Library of Congress Control Number')
    oclc = forms.CharField(required=False,
                           label='Online Computer Library Center number')

    def clean(self):
        super(GoogleForm, self).clean()
        has_values = len(['' for x in self.cleaned_data.values() if x != ''])
        if not has_values:
            self.add_error('intitle', 'At least one field must be filled')
