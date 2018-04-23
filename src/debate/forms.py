from django import forms


class NewComment(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)

    def comment_clean(self):
        comment = self.cleaned_data.get('comment')
        if comment == 'hi':
            raise forms.ValidationError('Error')
        return comment
