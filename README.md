
<p align="center">
<img src="docs/icon/icon.png" width="100%">
<br>
<h1 align="center">PythonDiagrammatic</h1>
<h2 align="center">～Sketch to Structure～</h2>
</p>

## 更新情報

- 2024-03-31
  - PlantUMLの説明を追加し、パッケージ情報をより明確にしました。
  - PlantUMLの使用に関する簡単なリファレンスと利用例を示しました。


## TODO

- [x] PlantUMLのサンプルコードを追加する。
- [ ] Diagramsのサンプルコードを追加する。
- [ ] Mermaidのサンプルコードを追加する。
- [ ] Graphvizのサンプルコードを追加する。
- [ ] NetworkXのサンプルコードを追加する。
- [ ] 新しいパッケージの紹介を検討する（リクエストがあれば）。
- [ ] ドキュメントの充実化を図る（使い方、サンプル図の追加など）。
- [ ] プロジェクトの機能拡張（新しいダイアグラムの種類、カスタマイズオプションなど）。
- [ ] コミュニティからのフィードバックを収集し、改善点を見出す。

## はじめに

PythonDiagrammaticは、Pythonを使ってシーケンス図や構成図などのダイアグラムを簡単に作成するためのプロジェクトです。
初心者でも直感的にダイアグラムを描けるように、人気のあるパッケージをいくつか紹介しています。

## 紹介するパッケージ

1. PlantUML:
   - PlantUMLは、シーケンス図、クラス図、アクティビティ図、コンポーネント図など様々なUML図を生成できるオープンソースツールです。
   - テキストベースの言語で図を記述し、それを図に変換します。
   - Pythonから使うには、`plantuml`パッケージをインストールします。
   - https://pypi.org/project/plantuml/

2. Diagrams:
   - Diagramsは、Pythonのコードを使ってシーケンス図、フローチャート、ネットワーク図などを作成するパッケージです。
   - シンプルで分かりやすいPythonコードで図を定義し、画像ファイルとして出力できます。 
   - https://pypi.org/project/diagrams/

3. Mermaid:
   - Mermaidは、マークダウンに似たシンプルな構文でフローチャート、シーケンス図、ガントチャートなどを作成するツールです。
   - Pythonから使うには、`mermaid-py`パッケージをインストールします。
   - https://pypi.org/project/mermaid-py/

4. Graphviz:
   - Graphvizは、グラフやネットワークを可視化するためのオープンソースツールです。
   - PythonからGraphvizを使うには、`graphviz`パッケージをインストールします。
   - DOT言語でグラフを定義し、画像ファイルとして出力します。
   - https://pypi.org/project/graphviz/

5. NetworkX:
   - NetworkXは、複雑なネットワークを分析・可視化するためのPythonパッケージです。
   - ネットワークやグラフの構造を定義し、様々なレイアウトアルゴリズムで可視化できます。
   - https://pypi.org/project/networkx/

## 使い方

各パッケージの基本的な使い方は、`examples`ディレクトリにサンプルコードがあります。
それぞれのサンプルを参考に、自分だけのダイアグラムを作ってみましょう！

## PlantUMLの使い方

ここでは、PlantUMLを使ってシーケンス図を作成する方法を紹介します。

![](examples/plantuml/sequence03.svg)

1. PlantUMLをインストールします。
   ```
   pip install plantuml
   ```

2. サンプルコードを実行します。
   ```
   python examples\plantuml\example03.py
   ```

3. カラーリストを確認します。
   - PlantUMLで使える色の一覧は、以下のリンクで確認できます。
   - https://github.com/qywx/PlantUML-colors/blob/master/plantuml-colors-notes.puml

4. 色の指定方法を確認します。
   - PlantUMLで色を指定する方法は、以下のリンクで確認できます。
   - https://plantuml.com/ja/color

5. 詳しくはこちら
   - [PlantUML Tutorial (examples/plantuml/README.md)](examples/plantuml/README.md)

## 今後の予定

- 他のパッケージのサンプルコードを追加していく予定です。
- リクエストがあれば、新しいパッケージの紹介も検討します。

ぜひPythonDiagrammaticを使って、楽しくダイアグラムを作ってみてください！
