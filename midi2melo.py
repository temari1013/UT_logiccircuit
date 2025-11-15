import mido

NOTE_NAMES = ['C', 'CS', 'D', 'DS', 'E', 'F', 'FS', 'G', 'GS', 'A', 'AS', 'B']

DEFAULT_TEMPO = 500000 

midi_file_path = '/Users/temari/Documents/Arduino/ex2.mid'  

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
        current_time_sec = 0.0
        last_event_time_sec = 0.0
        active_notes = {}
        track_notes_list = []

        track_name = track.name if track.name else f"Track {track_index + 1}"
        
        for msg in track:
            delta_time_sec = mido.tick2second(msg.time, mid.ticks_per_beat, current_tempo)
            current_time_sec += delta_time_sec
            if current_time_sec > last_event_time_sec:
                rest_duration_sec = current_time_sec - last_event_time_sec
                rest_duration_ms = int(rest_duration_sec * 1000)
                
                if rest_duration_ms > 0:
                    track_notes_list.append(('NA', rest_duration_ms))

            last_event_time_sec = current_time_sec

            if msg.is_meta:
                if msg.type == 'set_tempo':
                    current_tempo = msg.tempo
                continue
            

            if msg.type == 'note_on' and msg.velocity > 0:
                active_notes[msg.note] = current_time_sec


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

        converted_tracks_data[track_name] = track_notes_list

    return converted_tracks_data



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