# azureml-core of version 1.0.72 or higher is required
# azureml-dataprep[pandas] of version 1.1.34 or higher is required
from azureml.core import Workspace, Dataset

subscription_id = '653662f1-95de-4498-b876-1fd625bf5d18'
resource_group = 'udacityPlayGroundRG'
workspace_name = 'UdacityPGML'

workspace = Workspace(subscription_id, resource_group, workspace_name)

dataset = Dataset.get_by_name(workspace, name='bankmarketing')
dataset.to_pandas_dataframe()