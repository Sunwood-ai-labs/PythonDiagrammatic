from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Sample Web Service", show=False):
    lb = ELB("Load Balancer")
    
    with Cluster("Web Servers"):
        web_servers = [EC2("Web Server 1"),
                       EC2("Web Server 2"),
                       EC2("Web Server 3")]
    
    with Cluster("Database Cluster"):
        db_primary = RDS("Primary")
        db_replica = RDS("Replica")
        
    lb >> web_servers >> db_primary
    db_primary - db_replica