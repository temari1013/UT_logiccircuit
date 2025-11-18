playmelody:badapple!!!が流れる \
undead_score.txt : tonemelodyにコピペでアンデッドが流れる \
midi2melo.py: midiファイルを指定して実行すると休符に対応したtonemelodyにコピペして使える形式のスコアになる(多分) ≠
tonemelodyのヘッダファイルに、NAという音名と可聴域外の周波数を適当に指定すると休符になる(多分) 

追記:
可聴域外の音をそもそもaruduinoが再生できない(可聴域内の音が代わりに再生される)ので破綻
そもそもaruduino nano が同期に使えるIOを持ってない