from app import app,db,Student

students = [
    {"name":"Austin", "age":19, "teacher":"Solomon"},
    {"name":"Debra", "age":23, "teacher":"Nancy"},
    {"name":"Chris", "age":17, "teacher":"Fidel"},
    {"name":"Racheal", "age":24, "teacher":"Tinda"}
]

with app.app_context():
    for student in students:
        if not Student.query.filter_by(name=student["name"]).first():
            db.session.add(Student(**student))
            db.session.commit()
            print("seeding complete!")