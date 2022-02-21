from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title', 'text']
		labels = {
			'title': '',
			'text': '',
		}
		widgets = {
			'text': forms.Textarea(attrs={
				'cols': 120,
				'placeholder': 'Text...',
			}),
			'title': forms.TextInput(attrs={
				'placeholder': 'Title...',
			}),
		}