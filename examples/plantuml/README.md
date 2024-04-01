# PlantUML Tutorial

PlantUMLは、シンプルなテキストベースの言語を使ってUML図を描くことができるオープンソースツールです。Pythonから簡単にPlantUMLを使うことができ、シーケンス図やクラス図などを手軽に作成できます。

ここでは、PlantUMLを使ってシーケンス図を描く方法を、Pythonのサンプルコードを交えて解説していきます。

## 環境設定

まず、PlantUMLをPythonから使うために、`plantuml`パッケージをインストールします。

```bash

pip install plantuml
```

## 基本的なシーケンス図の描き方

PlantUMLでシーケンス図を描くには、`@startuml`と`@enduml`で図の範囲を指定し、その間にシーケンス図の要素を記述していきます。

以下は、クライアントとサーバー間の簡単なやり取りを表したシーケンス図の例です。

```python

from plantuml import PlantUML

server = PlantUML(url='http://www.plantuml.com/plantuml/svg/')

source = """
@startuml
participant Client
participant Server

Client -> Server: Request
activate Server
Server --> Client: Response
deactivate Server
@enduml
"""

output = server.processes(source)

with open('sequence.svg', 'wb') as f:
    f.write(output)
```

![file](https://hamaruki.com/wp-content/uploads/2024/03/image-1711883683232.png)

このコードでは、`PlantUML`クラスを使ってPlantUMLサーバーに接続し、`source`変数にシーケンス図の内容を記述しています。`processes`メソッドでソースコードを処理し、生成された画像を`sequence.svg`ファイルに保存しています。

## 複雑なシーケンス図の例

次に、もう少し複雑なシーケンス図の例を見てみましょう。


```python

from plantuml import PlantUML

server = PlantUML(url='http://www.plantuml.com/plantuml/svg/')

source = """
@startuml
actor 開発者
participant IssueWise
participant CommitCraft
participant DocuMind
participant GitHub
database リポジトリ

開発者 -> IssueWise : 1. オープンIssueを取得
IssueWise -> GitHub : GitHubからIssueを取得
GitHub --> IssueWise : Issueデータ
IssueWise --> 開発者 : Issueデータをマークダウン化

開発者 -> IssueWise : 2. AIにIssueとコードを入力
IssueWise -> DocuMind : コードの構造をマークダウン化
DocuMind -> リポジトリ : リポジトリの情報を取得
リポジトリ --> DocuMind : ファイル構造とコードスニペット
DocuMind --> IssueWise : マークダウン化されたコード
IssueWise --> 開発者 : マークダウン化された課題とコード

開発者 -> CommitCraft : 3. ステージング済み変更を取得  
CommitCraft -> リポジトリ : ステージング済み変更を取得
リポジトリ --> CommitCraft : 変更差分
CommitCraft --> 開発者 : 変更差分のマークダウン

開発者 -> CommitCraft : 4. AIにコミットメッセージを生成させる
CommitCraft --> 開発者 : コミットメッセージ

開発者 -> DocuMind : 5. ドキュメント化
DocuMind -> GitHub : 変更履歴を取得
GitHub --> DocuMind : コミットログ
DocuMind -> リポジトリ : リポジトリ情報を統合
リポジトリ --> DocuMind : ファイル構造とコードスニペット 
DocuMind --> 開発者 : マークダウン化されたドキュメント

@enduml
"""

output = server.processes(source)

with open('sequence02.svg', 'wb') as f:
    f.write(output)
```

このシーケンス図では、開発者とツール（IssueWise, CommitCraft, DocuMind）、そしてGitHubやリポジトリとの間のやり取りを表現しています。矢印（`->`）でメッセージの方向を示し、メッセージ名を記述することで、処理の流れを表現しています。

![file](https://hamaruki.com/wp-content/uploads/2024/03/image-1711883700045.png)

## シーケンス図のカスタマイズ

PlantUMLでは、シーケンス図の見た目をカスタマイズすることもできます。以下の例では、`skinparam`コマンドを使って、様々な要素の色や太さを変更しています。

```python

from plantuml import PlantUML

server = PlantUML(url='http://www.plantuml.com/plantuml/svg/')

source = """
@startuml

skinparam sequenceArrowThickness 3
skinparam ParticipantBorderColor LightCyan/CadetBlue
skinparam SequenceLifeLineBorderColor DarkCyan/CadetBlue
skinparam SequenceLifeLineBorderThickness 9
skinparam noteBorderColor Bisque/LightYellow
skinparam ActorBorderColor CadetBlue/LightSlateGray
skinparam ActorBackgroundColor Azure/LightSteelBlue

actor "<color:DarkSlateGray>開発者</color>" as 開発者 #Azure/LightSteelBlue
participant "<&SourceSage>SourceSage</&SourceSage>" as SourceSage #PowderBlue/LightPink
participant "<color:DarkSlateGray>IssueWise</color>" as IssueWise #MistyRose/LightSkyBlue
participant "<color:DarkSlateGray>CommitCraft</color>" as CommitCraft #PeachPuff/LightSteelBlue
participant "<color:DarkSlateGray>DocuMind</color>" as DocuMind #SeaShell/LightCoral
participant "<color:DarkSlateGray>GitHub</color>" as GitHub #Lavender/LightGoldenRodYellow
database "<color:DarkSlateGray>リポジトリ</color>" as リポジトリ #LavenderBlush/LightCyan

開発者 -> IssueWise : 1. オープンIssueを取得
IssueWise -> GitHub : GitHubからIssueを取得
GitHub --> IssueWise : Issueデータ
IssueWise --> 開発者 : Issueデータをマークダウン化

開発者 -> IssueWise : 2. AIにIssueとコードを入力
IssueWise -> DocuMind : コードの構造をマークダウン化
DocuMind -> リポジトリ : リポジトリの情報を取得
リポジトリ --> DocuMind : ファイル構造とコードスニペット
DocuMind --> IssueWise : マークダウン化されたコード
IssueWise --> 開発者 : マークダウン化された課題とコード

開発者 -> CommitCraft : 3. ステージング済み変更を取得  
CommitCraft -> リポジトリ : ステージング済み変更を取得
リポジトリ --> CommitCraft : 変更差分
CommitCraft --> 開発者 : 変更差分のマークダウン

開発者 -> CommitCraft : 4. AIにコミットメッセージを生成させる
CommitCraft --> 開発者 : コミットメッセージ

開発者 -> DocuMind : 5. ドキュメント化
DocuMind -> GitHub : 変更履歴を取得
GitHub --> DocuMind : コミットログ
DocuMind -> リポジトリ : リポジトリ情報を統合
リポジトリ --> DocuMind : ファイル構造とコードスニペット 
DocuMind --> 開発者 : マークダウン化されたドキュメント

@enduml
"""

output = server.processes(source)

with open('sequence03.svg', 'wb') as f:
    f.write(output)
```

この例では、矢印の太さ、参加者の枠線の色、ライフラインの色と太さ、ノートの枠線の色、アクターの枠線と背景色を変更しています。また、`<color>`タグを使って参加者の名前の色を指定したり、`#`に続けて色名を指定することで背景色を変更したりしています。

![file](https://hamaruki.com/wp-content/uploads/2024/03/image-1711883715093.png)

## まとめ

PlantUMLを使えば、シンプルなテキストベースの記法で様々なUML図を描くことができます。PythonからPlantUMLを使う方法を覚えておけば、シーケンス図やクラス図などを手軽に作成・更新できるようになるでしょう。




## リポジトリ

https://github.com/Sunwood-ai-labs/PythonDiagrammatic/tree/develop




ここで紹介した例を参考に、自分だけのシーケンス図を描いてみてください。色やスタイルをカスタマイズして、見やすく美しい図を作成しましょう。