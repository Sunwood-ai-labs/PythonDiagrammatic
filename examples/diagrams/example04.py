from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from urllib.request import urlretrieve

with Diagram("Custom with remote icons", show=False, filename="custom_remote", direction="LR"):

  # download the icon image file
  diagrams_url = "https://raw.githubusercontent.com/Sunwood-ai-labs/PythonDiagrammatic/feature/Diagrams/examples/diagrams/icon/diagrams_icon1.png"
  diagrams_icon = "diagrams.png"
  urlretrieve(diagrams_url, diagrams_icon)

  diagrams = Custom("Diagrams", diagrams_icon)

  with Cluster("Some Providers"):

    openstack_url = "https://raw.githubusercontent.com/Sunwood-ai-labs/PythonDiagrammatic/feature/Diagrams/examples/diagrams/icon/diagrams_icon2.png"
    openstack_icon = "openstack.png"
    urlretrieve(openstack_url, openstack_icon)

    openstack = Custom("OpenStack", openstack_icon)

    elastic_url = "https://raw.githubusercontent.com/Sunwood-ai-labs/PythonDiagrammatic/feature/Diagrams/examples/diagrams/icon/diagrams_icon3.png"
    elastic_icon = "elastic.png"
    urlretrieve(elastic_url, elastic_icon)

    elastic = Custom("Elastic", elastic_icon)

  diagrams >> openstack
  diagrams >> elastic