# NowPlaying-for-Mac

MacのiTunesで再生されいる音楽をTwitterへWebIntentsを経由してツイートします。

## 必要な環境

このプログラムはPython3の上で動きますので、Python3をインストールしてください。また、外部パッケージ「appscript」が必要です。

```
$ pip3 install appscript
```

## ショートカット化

Automatorを使えば、ショートカット化できます。指定したシェルスクリプトを実行するようにして、スクリプトを以下のようにすればショートカットができます。

```
$ /usr/local/bin/python3 Nowplaying.py
```
※Nowplaying.pyの部分は、パスをいれること。
