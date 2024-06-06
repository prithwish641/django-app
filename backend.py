import boto3
 
# AWS credentials
aws_access_key_id = 'AKIAQX2QOH26WKOQPCYN'
aws_secret_access_key = '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'
aws_region_name = 'us-east-1'
 
# Initialize a boto3 client for DevOps Guru with hardcoded credentials
devops_guru_client = boto3.client(
    'devops-guru',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region_name
)
 
def list_insights():
    insights_list = []  # List to hold insights dictionaries
    try:
        # Call the list_insights API to retrieve insights
        response = devops_guru_client.list_insights(
            StatusFilter={
                'Ongoing': {'Type': 'PROACTIVE'},
                # You can also filter by 'Closed' or 'Any' status
            }
        )
        # Print the entire response for debugging
        print("API Response:", response)
        # Check if the response contains proactive insights
        if 'ProactiveInsights' in response:
            for insight in response['ProactiveInsights']:
                insights_list.append(insight)
        # Check if the response contains reactive insights
        if 'ReactiveInsights' in response:
            for insight in response['ReactiveInsights']:
                insights_list.append(insight)
        if not insights_list:
            print("No insights found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return insights_list  # Return the list of insights dictionaries
 
# Call the function to list insights
insights = list_insights()
print(insights)
for insight in insights:
    print(insight)  # Print each insight dictionary