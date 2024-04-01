from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.vcs import Git
from diagrams.azure.compute import FunctionApps
from diagrams.azure.ml import MachineLearningServiceWorkspaces
from diagrams.aws.management import Cloudformation
from diagrams.aws.integration import StepFunctions

graph_attr = {
    "fontsize": "35",
    # "bgcolor": "transparent"
}

with Diagram("/app/examples/diagrams/examples03", show=False, filename="SourceSage_Architecture", direction="LR", graph_attr=graph_attr):

    github = Git("GitHub Repository")

    with Cluster("SourceSage"):
        main = FunctionApps("SourceSage.py")
        
        with Cluster("Modules"):
            modules = [
                FunctionApps("GitHubIssueRetrieve"),
                FunctionApps("StagedDiffGenerator"),
                FunctionApps("ChangelogGenerator"),
                FunctionApps("StageInfoGenerator"),
                FunctionApps("IssuesToMarkdown")
            ]
        
        outputs = Cloudformation("Generated Assets")

    claude = MachineLearningServiceWorkspaces("Claude AI")

    github >> Edge(color="lightblue", style="bold") >> main
    main >> Edge(color="lightgreen", style="bold") >> modules >> Edge(color="lightpink", style="bold") >> outputs
    outputs << Edge(color="lightyellow", style="bold") << StepFunctions("Feed") << Edge(color="lightsalmon", style="bold") << claude