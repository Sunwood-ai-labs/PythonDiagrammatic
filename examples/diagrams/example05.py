from diagrams import Diagram, Cluster
from diagrams.custom import Custom


with Diagram("Custom with local icons", show=False, filename="custom_local", direction="LR"):
  cc_heart = Custom("Creative Commons", "./examples/diagrams/icon/diagrams_icon1.png")
  cc_attribution = Custom("Credit must be given to the creator", "./examples/diagrams/icon/diagrams_icon2.png")

  cc_sa = Custom("Adaptations must be shared\n under the same terms", "./examples/diagrams/icon/diagrams_icon3.png")
  cc_nd = Custom("No derivatives or adaptations\n of the work are permitted", "./examples/diagrams/icon/diagrams_icon4.png")
  cc_zero = Custom("Public Domain Dedication", "./examples/diagrams/icon/diagrams_icon2.png")

  with Cluster("Non Commercial"):
    non_commercial = [Custom("Y", "./examples/diagrams/icon/diagrams_icon8.png") - Custom("E", "./examples/diagrams/icon/diagrams_icon7.png") - Custom("S", "./examples/diagrams/icon/diagrams_icon1.png")]

  cc_heart >> cc_attribution
  cc_heart >> non_commercial
  cc_heart >> cc_sa
  cc_heart >> cc_nd
  cc_heart >> cc_zero