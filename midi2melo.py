import mido

NOTE_NAMES = ['C', 'CS', 'D', 'DS', 'E', 'F', 'FS', 'G', 'GS', 'A', 'AS', 'B']

DEFAULT_TEMPO = 750000 

midi_file_path = '/Users/temari/Documents/Arduino/hotarunohikari.mid'  

def midi_to_note_duration_list(midi_file_path):

    try:
        mid = mido.MidiFile(midi_file_path)
    except FileNotFoundError:
        print(f"エラー: ファイル '{midi_file_path}' が見つかりません。")
        return {}
    except Exception as e:
        print(f"エラー: MIDIファイルの読み込み中に問題が発生しました: {e}")
        return {}

    converted_tracks_data = {}

    for track_index, track in enumerate(mid.tracks):
        current_tempo = DEFAULT_TEMPO
        current_time_sec = 0.0          # トラックの絶対時間（秒）
        last_event_time_sec = 0.0       # 最後にリストに追加された音符または休符の終了時刻
        active_notes = {}
        track_notes_list = []

        track_name = track.name if track.name else f"Track {track_index + 1}"
        
        for msg in track:
            # デルタタイムを秒単位に変換
            delta_time_sec = mido.tick2second(msg.time, mid.ticks_per_beat, current_tempo)
            
            # まず絶対時間をデルタタイム分進める
            current_time_sec += delta_time_sec

            # --- 1. メタメッセージの処理 ---
            if msg.is_meta:
                if msg.type == 'set_tempo':
                    current_tempo = msg.tempo
                continue
            
            # --- 2. ノートイベントの処理 ---
            
            # note_on (velocity > 0): 音符の開始
            if msg.type == 'note_on' and msg.velocity > 0:
                
                # --- ノートON前の休符処理 ---
                # ノートONイベント発生時刻と、最後にリストに追加されたイベントの終了時刻の差分が休符となる
                rest_duration_sec = current_time_sec - last_event_time_sec
                
                if rest_duration_sec > 0:
                    rest_duration_ms = int(rest_duration_sec * 1000)
                    if rest_duration_ms > 0:
                        track_notes_list.append(('NA', rest_duration_ms))
                        # 休符がリストに追加された場合、その休符の終了時刻（current_time_sec）が
                        # 次の音符/休符の開始時刻となるため、last_event_time_secを更新
                        last_event_time_sec = current_time_sec

                # ノート開始時間を記録
                active_notes[msg.note] = current_time_sec

            # note_off または note_on (velocity == 0): 音符の終了
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                if msg.note in active_notes:
                    note_start_time = active_notes.pop(msg.note)
                    note_duration_sec = current_time_sec - note_start_time

                    if note_duration_sec > 0:
                        note_number = msg.note
                        octave = note_number // 12 - 1 
                        note_name_raw = NOTE_NAMES[note_number % 12]
                        
                        note_label = f'NOTE_{note_name_raw}{octave}'
                        duration_ms = int(note_duration_sec * 1000)

                        track_notes_list.append((note_label, duration_ms))
                        
                        # ノートが終了した時刻を、次の休符の起点として記録
                        last_event_time_sec = current_time_sec

        converted_tracks_data[track_name] = track_notes_list

    return converted_tracks_data

# --- 実行部分（変更なし） ---

result = midi_to_note_duration_list(midi_file_path)

if result:
    print(f"--- MIDIファイル '{midi_file_path}' の変換結果 ---")
    for track_name, notes_list in result.items():
        print(f"\n## トラック: {track_name}")
    
        print("\n--- 変換結果 ---")
        c_code_output = []
        for note_label, duration_ms in notes_list:
            c_code_output.append(f"{{ {note_label}, {duration_ms} }}")
        
        print(',\n'.join(c_code_output))