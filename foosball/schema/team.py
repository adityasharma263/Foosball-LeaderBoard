from foosball.model.team import Team

from foosball import ma

class TeamSchema(ma.ModelSchema):

    class Meta:
        model = Team
        exclude = ('updated_at', 'created_at')