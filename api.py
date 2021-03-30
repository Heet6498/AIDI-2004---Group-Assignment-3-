from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

STUDENTS = {
  '1': {'firstname': 'Mark', 'lastname': 'Smith', 'dob': 'September 1 2000', 'amount': 1000},
  '2': {'firstname': 'Sam', 'lastname': 'Johnson', 'dob': 'January 19 1999', 'amount': 1500},
  '3': {'firstname': 'Jake', 'lastname': 'Robinson', 'dob': 'June 14 1996', 'amount': 1100},
  '4': {'firstname': 'Mike', 'lastname': 'Williams', 'dob': 'November 22 1997', 'amount': 1300},
}

parser = reqparse.RequestParser()

class StudentsList(Resource):
    def get(self):
          return STUDENTS
    def post(self):
          parser.add_argument("firstname")
          parser.add_argument("lastname")
          parser.add_argument("dob")
          parser.add_argument("amount")
          args = parser.parse_args()
          student_id = int(max(STUDENTS.keys())) + 1
          student_id = '%i' % student_id
          STUDENTS[student_id] = {
            "firstname": args["firstname"],
            "lastname": args["lastname"],
            "dob": args["dob"],
            "amount:": args["amount"]
          }
          return STUDENTS[student_id], 201

class Student(Resource):
        def get(self, student_id):
              if student_id not in STUDENTS:
                  return "Not found", 404
              else:
                  return STUDENTS[student_id]
              
        def put(self, student_id):
              parser.add_argument("firstname")
              parser.add_argument("lastname")
              parser.add_argument("dob")
              parser.add_argument("amount")
              args = parser.parse_args()
              if student_id not in STUDENTS:
                return "Record not found", 404
              else:
                student = STUDENTS[student_id]
                student["firstname"] = args["firstname"] if args["firstname"] is not None else student["firstname"]
                student["lastname"] = args["lastname"] if args["lastname"] is not None else student["lastname"]
                student["dob"] = args["dob"] if args["dob"] is not None else student["dob"]
                student["amount"] = args["amount"] if args["amount"] is not None else student["amount"]
                return student, 200
            
        def delete(self, student_id):
              if student_id not in STUDENTS:
                  return "Not found", 404
              else:
                  del STUDENTS[student_id]
                  return '', 204

api.add_resource(StudentsList, '/students/')
api.add_resource(Student, '/students/<student_id>')

if __name__=='__main__':
    app.run(debug=True)