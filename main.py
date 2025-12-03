import nemain

@nemain.save_log('add_note')
def add_note(title, text):
    notes = nemain.load_notes()
    new_id = max([note['id'] for note in notes], default=0) + 1
    note = {
        'id': new_id,
        'title': title,
        'text': text
    }
    notes.append(note)
    nemain.save_notes(notes)
    print(f"Заметка '{title}' добавлена (id: {new_id})")
    return new_id

@nemain.save_log('get_note')
def get_note(id):
    notes = nemain.load_notes()
    for note in notes:
        if note['id'] == id:
            print(f"Найдена заметка: {note['title']}")
            return note
    print(f"Заметка с id {id} не найдена")
    return None

@nemain.save_log('delete_note')
def delete_note(id):
    notes = nemain.load_notes()
    new_notes = [note for note in notes if note['id'] != id]
    if len(new_notes) == len(notes):
        print(f"Заметка с id {id} не найдена")
        return False
    nemain.save_notes(new_notes)
    print(f"Заметка с id {id} удалена")
    return True

if __name__ == '__main__':
    add_note("фурри", "погладить котика")
    add_note("христмас", "повесить гирлянду")

    note = get_note(2)
    if note:
        print(f"Текст заметки: {note['text']}")

    delete_note(1)