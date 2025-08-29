from models import NoteModel

notes_list = [
    NoteModel(
        title="A Test Study Note",
        content="**Haha, I am definitely studying (for real).**",
        collection_id=1,
        owner_id=1,
    ),
    NoteModel(
        title="A Test No Collection Note",
        content="**I should also be a valid note, please and thank you.**",
        owner_id=2,
    ),
    NoteModel(
        title="A Test Cooking Note To The Wrong Collection Owner",
        content="**I am a cooking note, I guess.**",
        owner_id=1,
    ),
    NoteModel(
        title="A Test Linux Note",
        content="**I should also be a valid note, please and thank you.**",
        collection_id=3,
        owner_id=1,
    ),
    NoteModel(
        title="Another Test Linux Note",
        content="**I should also be a valid note, please and thank you.**",
        collection_id=3,
        owner_id=1,
    ),
]
