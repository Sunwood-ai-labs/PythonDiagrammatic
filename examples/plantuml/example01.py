"""PlantUMLのシーケンス図を生成するサンプル"""
from plantuml import PlantUML

# PlantUMLサーバーのURLを指定
server = PlantUML(url='http://www.plantuml.com/plantuml/svg/')

# シーケンス図のソースコードを定義
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

# 画像を生成
output = server.processes(source)

# 生成された画像を'sequence.svg'ファイルに保存
with open('sequence.svg', 'wb') as f:
    f.write(output)

print("Success!")