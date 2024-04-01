# Diagrams Tutorial

Diagramsは、Pythonのコードを使ってシーケンス図、フローチャート、ネットワーク図などを作成するパッケージです。このガイドでは、初心者でも簡単にDiagramsを使いこなせるように、丁寧に説明していきます。

## インストール方法

Diagramsを使うには、以下のコマンドでパッケージをインストールします。

```bash
pip install diagrams
```

### ローカル環境の場合

Diagramsを使うには、Graphvizというツールが必要です。以下のリンクからGraphvizをダウンロードしてインストールしてください。

https://graphviz.org/download/

### Dockerを使う場合

Dockerを使う場合は、以下のコマンドでDockerイメージを起動します。

```bash
docker-compose up
```

## 基本的な使い方

### example01.py

```python

from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("/app/examples/diagrams/examples01", show=False):
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
```

このコードは、AWSのアーキテクチャを表現したシンプルな例です。

1. 必要なクラスをインポートします。

```python
from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS 
from diagrams.aws.network import ELB
```

2. `Diagram`クラスを使って図全体の設定を行います。

```python
with Diagram("/app/examples/diagrams/examples01", show=False):
```
- 第1引数は図の出力先パス、`show=False`は図を自動で表示しないという設定です。

3. ロードバランサーを表す`ELB`ノードを定義します。

```python
lb = ELB("Load Balancer")
```

4. ウェブサーバーのクラスターを定義します。

```python
with Cluster("Web Servers"):
web_servers = [EC2("Web Server 1"),
EC2("Web Server 2"),
EC2("Web Server 3")]
```
- クラスター内のノードは、インデントを使って表現します。

5. データベースクラスターを定義します。

```python
with Cluster("Database Cluster"):
db_primary = RDS("Primary") 
db_replica = RDS("Replica")
```

6. ノード間の関係を定義します。

```python
lb >> web_servers >> db_primary
db_primary - db_replica  
```
- `>>`は「から」「へ」の関係、`-`は双方向の関係を表します。

コードを実行すると、指定したパスに図が生成されます。

![](https://hamaruki.com/wp-content/uploads/2024/04/examples01.png)


## より複雑な例


### example02.py

```python
from diagrams import Cluster, Diagram
from diagrams.onprem.vcs import Git
from diagrams.azure.compute import FunctionApps
from diagrams.azure.ml import MachineLearningServiceWorkspaces
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

    claude = MachineLearningServiceWorkspaces("Claude AI")

    github >> main
    main >> modules >> outputs
    outputs << StepFunctions("Feed") << claude
```

このコードは、SourceSageというプロジェクトのアーキテクチャを表現した例です。

1. 必要なクラスをインポートします。

```python
from diagrams import Cluster, Diagram
from diagrams.onprem.vcs import Git
from diagrams.azure.compute import FunctionApps
from diagrams.azure.ml import MachineLearningServiceWorkspaces
from diagrams.aws.management import Cloudformation
from diagrams.aws.integration import StepFunctions
```

2. 図全体の属性を設定します。

   ```python
   graph_attr = {
       "fontsize": "35", 
       # "bgcolor": "transparent"
   }
   ```

3. `Diagram`クラスを使って図全体の設定を行います。

   ```python
   with Diagram("/app/examples/diagrams/examples02", show=False, filename="SourceSage_Architecture", direction="LR", graph_attr=graph_attr):
   ```
   - `direction="LR"`で、図を左から右に流れるように設定しています。

4. GitHubリポジトリを表すノードを定義します。

   ```python
   github = Git("GitHub Repository")
   ```

5. SourceSageのメインモジュールとサブモジュールを定義します。

   ```python
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
   ```

6. Claude AIを表すノードを定義します。

   ```python
   claude = MachineLearningServiceWorkspaces("Claude AI")
   ```

7. ノード間の関係を定義します。

   ```python
   github >> main
   main >> modules >> outputs
   outputs << StepFunctions("Feed") << claude
   ```

コードを実行すると、指定したパスに図が生成されます。

![](https://hamaruki.com/wp-content/uploads/2024/04/examples02.png)

### example03.py

```python
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
```

このコードは、example02.pyとほぼ同じですが、ノード間の関係を表す矢印にカスタムスタイルを適用しています。

1. 必要なクラスをインポートします。

   ```python
   from diagrams import Cluster, Diagram, Edge
   from diagrams.onprem.vcs import Git
   from diagrams.azure.compute import FunctionApps
   from diagrams.azure.ml import MachineLearningServiceWorkspaces
   from diagrams.aws.management import Cloudformation
   from diagrams.aws.integration import StepFunctions
   ```
   - `Edge`クラスを追加でインポートしています。

2. 図全体の属性を設定します。（example02.pyと同じ）

3. `Diagram`クラスを使って図全体の設定を行います。（example02.pyと同じ）

4. GitHubリポジトリを表すノードを定義します。（example02.pyと同じ）

5. SourceSageのメインモジュールとサブモジュールを定義します。（example02.pyと同じ）

6. Claude AIを表すノードを定義します。（example02.pyと同じ）

7. ノード間の関係を定義します。ここで`Edge`クラスを使ってスタイルを適用しています。

   ```python
   github >> Edge(color="lightblue", style="bold") >> main
   main >> Edge(color="lightgreen", style="bold") >> modules >> Edge(color="lightpink", style="bold") >> outputs
   outputs << Edge(color="lightyellow", style="bold") << StepFunctions("Feed") << Edge(color="lightsalmon", style="bold") << claude
   ```
   - `Edge`クラスの引数で色やスタイルを指定しています。

コードを実行すると、指定したパスに図が生成されます。矢印にカスタムスタイルが適用されているのが分かります。

![](https://hamaruki.com/wp-content/uploads/2024/04/examples03.png)


## カスタムアイコンを使う


### example04.py

```python
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
```

このコードは、リモートのカスタムアイコンを使って図を作成する例です。

1. 必要なクラスをインポートします。

   ```python
   from diagrams import Diagram, Cluster
   from diagrams.custom import Custom
   from urllib.request import urlretrieve
   ```
   - `Custom`クラスを使ってカスタムアイコンを定義します。
   - `urlretrieve`関数を使ってリモートのアイコン画像をダウンロードします。

2. `Diagram`クラスを使って図全体の設定を行います。

   ```python
   with Diagram("Custom with remote icons", show=False, filename="custom_remote", direction="LR"):
   ```

3. Diagramsのアイコンをダウンロードし、`Custom`クラスを使ってノードを定義します。

   ```python
   diagrams_url = "https://raw.githubusercontent.com/Sunwood-ai-labs/PythonDiagrammatic/feature/Diagrams/examples/diagrams/icon/diagrams_icon1.png"
   diagrams_icon = "diagrams.png"
   urlretrieve(diagrams_url, diagrams_icon)

   diagrams = Custom("Diagrams", diagrams_icon)
   ```

4. OpenStackとElasticのアイコンをダウンロードし、`Custom`クラスを使ってノードを定義します。

   ```python
   with Cluster("Some Providers"):

     openstack_url = "https://raw.githubusercontent.com/Sunwood-ai-labs/PythonDiagrammatic/feature/Diagrams/examples/diagrams/icon/diagrams_icon2.png"
     openstack_icon = "openstack.png"
     urlretrieve(openstack_url, openstack_icon)

     openstack = Custom("OpenStack", openstack_icon)

     elastic_url = "https://raw.githubusercontent.com/Sunwood-ai-labs/PythonDiagrammatic/feature/Diagrams/examples/diagrams/icon/diagrams_icon3.png"
     elastic_icon = "elastic.png"
     urlretrieve(elastic_url, elastic_icon)

     elastic = Custom("Elastic", elastic_icon)
   ```

5. ノード間の関係を定義します。

   ```python
   diagrams >> openstack
   diagrams >> elastic
   ```

コードを実行すると、指定したパスに図が生成されます。リモートのカスタムアイコンが使われているのが分かります。

![](https://hamaruki.com/wp-content/uploads/2024/04/examples04.png)



### example05.py

```python
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
```

このコードは、ローカルのカスタムアイコンを使ってCreative Commonsのライセンスを表現した例です。

1. 必要なクラスをインポートします。

   ```python
   from diagrams import Diagram, Cluster
   from diagrams.custom import Custom
   ```

2. `Diagram`クラスを使って図全体の設定を行います。

   ```python
   with Diagram("Custom with local icons", show=False, filename="custom_local", direction="LR"):
   ```

3. Creative Commonsのアイコンを`Custom`クラスを使って定義します。

   ```python
   cc_heart = Custom("Creative Commons", "./examples/diagrams/icon/diagrams_icon1.png")
   cc_attribution = Custom("Credit must be given to the creator", "./examples/diagrams/icon/diagrams_icon2.png")

   cc_sa = Custom("Adaptations must be shared\n under the same terms", "./examples/diagrams/icon/diagrams_icon3.png")
   cc_nd = Custom("No derivatives or adaptations\n of the work are permitted", "./examples/diagrams/icon/diagrams_icon4.png")
   cc_zero = Custom("Public Domain Dedication", "./examples/diagrams/icon/diagrams_icon2.png")
   ```
   - 各アイコンのパスを指定して、`Custom`クラスでノードを定義しています。

4. "Non Commercial"クラスターを定義します。

   ```python
   with Cluster("Non Commercial"):
     non_commercial = [Custom("Y", "./examples/diagrams/icon/diagrams_icon8.png") - Custom("E", "./examples/diagrams/icon/diagrams_icon7.png") - Custom("S", "./examples/diagrams/icon/diagrams_icon1.png")]
   ```
   - クラスター内のノードを`-`で連結しています。

5. ノード間の関係を定義します。

   ```python
   cc_heart >> cc_attribution
   cc_heart >> non_commercial
   cc_heart >> cc_sa
   cc_heart >> cc_nd 
   cc_heart >> cc_zero
   ```

コードを実行すると、指定したパスに図が生成されます。ローカルのカスタムアイコンを使ってCreative Commonsのライセンスが表現されています。

![](https://hamaruki.com/wp-content/uploads/2024/04/examples05.png)

以上が、5つの例の詳細な解説です。これらの例を参考に、自分だけの図を作ってみてください。

Diagramsは、Pythonのコードを使って簡単に図を作成できるパワフルなツールです。以下の点を押さえておくと、より効果的に活用できるでしょう。

- `Diagram`クラスで図全体の設定を行う
- `Cluster`クラスでノードをグループ化する
- `Custom`クラスでカスタムアイコンを使う
- `Edge`クラスでノード間の関係にスタイルを適用する
- ノード間の関係は`>>`や`-`などの演算子で表現する

これらの機能を組み合わせることで、複雑なアーキテクチャやワークフローを分かりやすく可視化できます。ぜひ、Diagramsを使ってあなたのアイデアを図に表現してみてください！


## まとめ

- Diagramsは、Pythonのコードを使って図を作成するパッケージ
- インストールは`pip install diagrams`で行う
- ローカル環境ではGraphvizが必要、Dockerを使う方法もある
- `Diagram`クラスで図全体の設定、`Cluster`で要素をグループ化
- `>>`や`-`などの演算子で要素間の関係を定義
- `Custom`クラスでカスタムアイコンを使える

以上が、Diagramsの基本的な使い方です。この知識を元に、自分だけの図を作ってみてください。徐々に複雑な図にチャレンジしていきましょう！