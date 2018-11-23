from django import forms

from .models import Records, Comments


class CreateRecordForm(forms.ModelForm):

    class Meta:
        model = Records
        fields = ['title', 'descripcion', 'upload']
        labels = { 'title': 'Titulo', 'descripcion': 'Descripcion', 'upload': 'Subir Audio' }
        widgets = { 'descripcion': forms.Textarea(
                        attrs={'width':"70%", 'cols' : "50", 'rows': "4", })
                  }


class CommentsForm(forms.ModelForm):

    class Meta():
        model = Comments
        fields = ['comment']
        widgets = { 'comment': forms.Textarea(
                        attrs={'width':"70%", 'cols' : "50", 'rows': "4", })
                  }
