from django import forms
from .models import Records, Comments

from django.forms.utils import ErrorList

#only valadate extension, that can be change.
from django.core.validators import FileExtensionValidator

import os

class CreateRecordForm(forms.ModelForm):
    ALLOWED_TYPES = ['mp3', 'wav']
    class Meta:
        model = Records
        fields = ['title', 'descripcion', 'upload']
        labels = { 'title': 'Titulo', 'descripcion': 'Descripcion',
                                                'upload': 'Subir Audio' }
        widgets = { 'descripcion': forms.Textarea(
                        attrs={'width':"70%", 'cols' : "50", 'rows': "4", })
                  }

    def clean_upload(self):
        upload = self.cleaned_data['upload']
        # 5MB - 5242880
        extension = os.path.splitext(upload.name)[1][1:].lower()
        if upload.size > 5242880 or (extension not in self.ALLOWED_TYPES):
            if upload.size > 5242880:
               self.errors["upload"] = ErrorList(
                                [u"La grabacion tiene que ser menor de 5 MB."])
            else:
                self.errors["upload"] = ErrorList(
                  [u"Archivo de audio no tiene formato permitido mp3 or wav."])
        else:
            return upload

class CommentsForm(forms.ModelForm):

    class Meta():
        model = Comments
        fields = ['comment']
        widgets = { 'comment': forms.Textarea(
                        attrs={'width':"70%", 'cols' : "50", 'rows': "4", })
                  }
