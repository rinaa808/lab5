from flask import Blueprint
from app.models import Employee, Position, Division, Job
from app import db


bp = Blueprint('bp', __name__)


@bp.route('/', methods=['GET'])
def add_employee():
    employee_data = {
        "name": "Evgeny",
        "surname": "Baranov",
        "address": "Voroshilova20",
        "patronymic": "Alekseevich",
        "date_of_birth": "1999-03-01"
    }
    try:
        new_employee = Employee(**employee_data)
        db.session.add(new_employee)
        db.session.commit()
    except Exception as ex:
        print(type(ex))

    return 'new employee'


@bp.route('/', methods=['GET'])
def get_employee():

    employee = Employee.query.get(2)
    try:
        print("Name of employee: ", employee.name,
          " Surname: ", employee.surname,
          " Patronymic: ", employee.patronymic,
          " Address: ", employee.address,
          " Date of birth: ", employee.date_of_birth)
    except Exception as ex:
        print(type(ex))

    return 'hi'


@bp.route('/', methods=['GET'])
def delete_employee():

    employee = Employee.query.get(4)
    try:
        db.session.delete(employee)
        db.session.commit()
    except Exception as ex:
        print(type(ex))

    return 'employee was delete'


@bp.route('/', methods=['GET'])
def edit_employee():

    employee = Employee.query.get(3)
    try:
        employee.surname = 'Borisov'
        db.session.add(employee)
        db.session.commit()
    except Exception as ex:
        print(type(ex))

    return 'hi'

@bp.route('/', methods=['GET'])
def add_position():
    position_data = {
        "title": "Operator"
    }

    try:
        new_position = Position(**position_data)
        db.session.add(new_position)
        db.session.commit()
    except Exception as ex:
        print(type(ex))

    return 'new position'


@bp.route('/', methods=['GET'])
def get_position():

    position = Position.query.get(2)
    try:
        print("Title of position: ", position.title)
    except Exception as ex:
        print(type(ex))

    return 'hi'


@bp.route('/', methods=['GET'])
def delete_position():

    position = Position.query.get(4)
    try:
        db.session.delete(position)
        db.session.commit()
    except Exception as ex:
        print(type(ex))

    return 'position was delete'


@bp.route('/', methods=['GET'])
def add_division():
    division_data = {
        "title": "Div1"
    }

    try:
        new_division = Division(**division_data)
        db.session.add(new_division)
        db.session.commit()
    except Exception as ex:
        print(type(ex))

    return 'new division'


@bp.route('/', methods=['GET'])
def get_division():

    division = Division.query.get(2)
    try:
        print("Title of division: ", division.title)
    except Exception as ex:
        print(type(ex))

    return 'hi'


@bp.route('/', methods=['GET'])
def delete_division():

    division = Division.query.get(4)
    try:
        db.session.delete(division)
        db.session.commit()
    except Exception as ex:
        print(type(ex))

    return 'division was delete'


@bp.route('/', methods=['GET'])
def employment():

    employee = Employee.query.get(5)
    position = Position.query.get(1)
    division = Division.query.get(1)

    employment_data = {
        "staffer_id": employee.id,
        "position_id": position.id,
        "division_id": division.id,
        "date_of_employment": "2020-09-09"
    }

    try:
        new_employment = Job(**employment_data)
        db.session.add(new_employment)
        db.session.commit()
    except Exception as ex:
        print(type(ex))

    return 'new employment'


@bp.route('/', methods=['GET'])
def dismissal():

    try:
        job = Job.query.filter(Job.staffer_id == 1).one()
        job.date_of_dismissal = '2021-09-09'
        db.session.add(job)
        db.session.commit()
    except Exception as ex:
        print(type(ex))

    return 'hi'

@bp.route('/', methods=['GET'])
def get_list_of_employees():

    # employees = Employee.query.join(Job).filter(Job.date_of_dismissal == None).all()
    try:
        print("List of employees: ",
              Employee.query.join(Job).filter(Job.date_of_dismissal == None).order_by(Job.date_of_employment).all())
    except Exception as ex:
        print(type(ex))

    return 'hi'

