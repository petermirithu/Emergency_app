class Emergency(db.Model):
    __tablename__ = 'emergency'

    id = db.Column(db.Integer,primary_key =True)
    victim = db.Column(db.String,index = True)
    category = db.Column(db.String)
    description = db.Column(db.String)

    # save emergency
    def save_emergency(self):
        db.session.add(self)
        db.session.commit()

    # get all emergencies
    def get_emergencies():
        emergencies = Emergency.query.all()
        return emergencies
    