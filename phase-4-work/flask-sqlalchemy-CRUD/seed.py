from app import app,db,River

rivers = [
    {"name" : "Yala", "source" : "Nandi escarpments", "length_in_km" : 219},
    {"name" : "Nzoia", "source" : "Cherangany Hills", "length_in_km" : 257},
    {"name" : "Nairobi", "source" : "Ondiri Swamp", "length_in_km" : 390},
    {"name" : "Tana", "source" : "Aberdare Mountains", "length_in_km" : 1000},
]

with app.app_context():
    for river in rivers:
        if not River.query.filter_by(name=river["name"]).first():
            db.session.add(River(**river))
            db.session.commit()
            print("Seeding complete!")
