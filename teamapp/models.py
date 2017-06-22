from mongoengine import Document, EmbeddedDocument, fields


class Member(EmbeddedDocument):
    id = fields.StringField(required=True)
    username = fields.StringField(required=True)


class Team(Document):

    id = fields.StringField(required=True, primary_key=True)
    team_name = fields.StringField(required=True)
    members = fields.EmbeddedDocumentListField(Member)
