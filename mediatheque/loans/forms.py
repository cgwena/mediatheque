from django import forms

from loans.models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ("emprunteur", "date")
