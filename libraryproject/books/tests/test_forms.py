import pytest

from books import forms


def test_Google_form_clean(form_data):
    form = forms.GoogleForm(data=form_data)
    form.is_valid()
    form.clean()
    assert form.errors == {}


def test_Google_form_clean_with_some_missing_data(form_data):
    form_data['intitle'] = ''
    form_data['language'] = ''
    form_data['inpublisher'] = ''
    form = forms.GoogleForm(data=form_data)
    form.is_valid()
    form.clean()
    assert form.errors == {}


def test_Google_form_clean_with_empty_data(form_empty_data):
    form = forms.GoogleForm(data=form_empty_data)
    form.is_valid()
    form.clean()
    assert 'intitle' in form.errors
