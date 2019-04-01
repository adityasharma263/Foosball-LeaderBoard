# -*- coding: utf-8 -*-
from foosball import db
from foosball.model.base import Base


class Team(Base):
    __tablename__ = 'team'

    first_player_name = db.Column(db.String, nullable=False)
    second_player_name = db.Column(db.String, nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<score %r>' % self.score