from django import forms

class AwsCredentialsForm(forms.Form):
    aws_account_id = forms.CharField(
        label='AWS Account ID',
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your AWS Account ID'})
    )
    aws_secret_key = forms.CharField(
        label='AWS Secret Key',
        max_length=40,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your AWS Secret Key'})
    )
    aws_access_key = forms.CharField(
        label='AWS Access Key',
        max_length=20,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your AWS Access Key'})
    )