from .models import Profile

class BooksSearchListView(forms.ModelForm):

    query = forms.TextField()

    class Meta:
        model = Profile
        fields = ('search')
