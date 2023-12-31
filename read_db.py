from db.models import Notes, Record, Tag
import db.connect


# notes = Notes.objects()
# for note in notes:
#     print("-------------------")
#     records = [
#         f"description: {record.description}, done: {record.done}"
#         for record in note.records
#     ]
#     tags = [tag.name for tag in note.tags]
#     print(
#         f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}"
#     )
notes = Notes.objects()
print("-------------------")
for note in notes:
    print(note.to_mongo().to_dict())

notes = Notes.objects(tags__name="Fun")
for note in notes:
    records = [
        f"description: {record.description}, done: {record.done}"
        for record in note.records
    ]
    tags = [tag.name for tag in note.tags]
    print(
        f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}"
    )
