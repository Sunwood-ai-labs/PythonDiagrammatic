"""PlantUMLのシーケンス図を生成するサンプル"""
from plantuml import PlantUML

# PlantUMLサーバーのURLを指定
server = PlantUML(url='http://www.plantuml.com/plantuml/svg/')

# シーケンス図のソースコードを定義
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

# 画像を生成
output = server.processes(source)

# 生成された画像を'sequence.svg'ファイルに保存
with open('sequence03.svg', 'wb') as f:
    f.write(output)

print("Success!")