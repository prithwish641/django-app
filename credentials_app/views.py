# credentials_app/views.py
from django.shortcuts import render
from .forms import AwsCredentialsForm
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def get_insights(aws_access_key_id, aws_secret_access_key, aws_region_name):
    reactive_insights_list = []
    proactive_insights_list = []
    try:
        devops_guru_client = boto3.client(
            'devops-guru',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region_name
        )
        # Retrieve reactive insights
        reactive_response = devops_guru_client.list_insights(
            StatusFilter={'Ongoing': {'Type': 'REACTIVE'}}
        )
        reactive_insights_list.extend(reactive_response.get('ReactiveInsights', []))
        
        # Retrieve proactive insights
        proactive_response = devops_guru_client.list_insights(
            StatusFilter={'Ongoing': {'Type': 'PROACTIVE'}}
        )
        proactive_insights_list.extend(proactive_response.get('ProactiveInsights', []))
        
    except Exception as e:
        print(f"An error occurred: {e}")
    return reactive_insights_list, proactive_insights_list

def index(request):
    form = AwsCredentialsForm()
    if request.method == 'POST':
        form = AwsCredentialsForm(request.POST)
        if form.is_valid():
            # Hardcoded AWS credentials (use only for demonstration purposes)
            aws_access_key_id = 'AKIAQX2QOH26WKOQPCYN'
            aws_secret_access_key = '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'
            aws_region_name = 'us-east-1'
            reactive_insights, proactive_insights = get_insights(aws_access_key_id, aws_secret_access_key, aws_region_name)
            return render(request, 'insights.html', {
                'reactive_insights': reactive_insights,
                'proactive_insights': proactive_insights
            })
    return render(request, 'index.html', {'form': form})

