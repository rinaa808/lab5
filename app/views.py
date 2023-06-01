from flask import Blueprint
from app.models import Employee, Position, Division, Job
from app import db
from flask import request
from flask import abort

bp = Blueprint('bp', __name__)


@bp.route('/employee/add', methods=['GET'])
def add_employee():
    employee_data = {
        "name": request.args.get('name'),
        "surname": request.args.get('surname'),
        "address": request.args.get('address'),
        "patronymic": request.args.get('patronymic'),
        "date_of_birth": request.args.get('date_of_birth')
    }
    try:
        new_employee = Employee(**employee_data)
        db.session.add(new_employee)
        db.session.commit()
    except Exception as ex:
        print(type(ex))


@bp.route('/employee/get', methods=['GET'])
def get_employee():
    employee = Employee.query.get(request.args.get('id'))
    print("Name of employee: ", employee.name,
          " Surname: ", employee.surname,
          " Patronymic: ", employee.patronymic,
          " Address: ", employee.address,
          " Date of birth: ", employee.date_of_birth)

    if not employee:
        abort(404)
    return dict(employee)


@bp.route('/employee/delete', methods=['DELETE'])
def delete_employee():
    employee = Employee.query.get(request.args.get('id'))
    db.session.delete(employee)
    db.session.commit()

    if not employee:
        abort(404)
    return dict(employee)


@bp.route('/employee/edit', methods=['PUT'])
def edit_employee():
    employee = Employee.query.get(request.args.get('id'))
    employee.surname = request.args.get('surname')
    db.session.add(employee)
    db.session.commit()

    if not employee:
        abort(404)
    return dict(employee)


@bp.route('/position/add', methods=['POST'])
def add_position():
    position_data = {
        "title": request.args.get('title')
    }

    try:
        new_position = Position(**position_data)
        db.session.add(new_position)
        db.session.commit()
    except Exception as ex:
        print(type(ex))


@bp.route('/position/get', methods=['GET'])
def get_position():
    position = Position.query.get(request.args.get('id'))
    print("Title of position: ", position.title)

    if not position:
        abort(404)
    return dict(position)


@bp.route('/position/delete', methods=['DELETE'])
def delete_position():
    position = Position.query.get(request.args.get('id'))
    db.session.delete(position)
    db.session.commit()

    if not position:
        abort(404)
    return dict(position)


@bp.route('/division/add', methods=['POST'])
def add_division():
    division_data = {
        "title": request.args.get('title')
    }

    try:
        new_division = Division(**division_data)
        db.session.add(new_division)
        db.session.commit()
    except Exception as ex:
        print(type(ex))


@bp.route('/division/get', methods=['GET'])
def get_division():
    division = Division.query.get(request.args.get('id'))
    print("Title of division: ", division.title)

    if not division:
        abort(404)
    return dict(division)


@bp.route('/division/delete', methods=['DELETE'])
def delete_division():
    division = Division.query.get(request.args.get('id'))
    db.session.delete(division)
    db.session.commit()

    if not division:
        abort(404)
    return dict(division)


@bp.route('/employment', methods=['POST'])
def employment():
    employee = Employee.query.get(request.args.get('employee_id'))
    position = Position.query.get(request.args.get('position_id'))
    division = Division.query.get(request.args.get('division_id'))

    employment_data = {
        "staffer_id": request.args.get(employee.id),
        "position_id": request.args.get(position.id),
        "division_id": request.args.get(division.id),
        "date_of_employment": request.args.get('date_of_employment')
    }

    new_employment = Job(**employment_data)
    db.session.add(new_employment)
    db.session.commit()

    if not employee or not position or not division:
        abort(404)
    return dict(division)


@bp.route('/dismissal', methods=['PUT'])
def dismissal():
    try:
        job = Job.query.filter(Job.staffer_id == 1).one()
        job.date_of_dismissal = request.args.get('date_of_dismissal')
        db.session.add(job)
        db.session.commit()
    except Exception as ex:
        print(type(ex))

    return 'hi'


@bp.route('/employees', methods=['GET'])
def get_list_of_employees():
    employees = Employee.query.join(Job).filter(Job.date_of_dismissal == "None").order_by(Job.date_of_employment).all()
    print("List of employees: ", employees)

    if not employees:
        abort(404)
    return dict(employees)
