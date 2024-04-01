from diagrams import Cluster, Diagram
from diagrams.onprem.vcs import Git
from diagrams.azure.compute import FunctionApps
from diagrams.azure.ml import MachineLearningServiceWorkspaces  # 変更
from diagrams.aws.management import Cloudformation
from diagrams.aws.integration import StepFunctions

graph_attr = {
    "fontsize": "35",
    # "bgcolor": "transparent"
}

with Diagram("/app/examples/diagrams/examples02", show=False, filename="SourceSage_Architecture", direction="LR", graph_attr=graph_attr):

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

    claude = MachineLearningServiceWorkspaces("Claude AI")  # 変更

    github >> main
    main >> modules >> outputs
    outputs << StepFunctions("Feed") << claude