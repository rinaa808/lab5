from flask import Blueprint, render_template, request, abort
from app.models import Employee, Position, Division, Job
from app import db
from flask_login import login_required, current_user

bp = Blueprint('bp', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


# @bp.route('/profile')
# @login_required
# def profile():
#     return render_template('employees.html', name=current_user.name)


@bp.route('/employees', methods=['GET'])
@login_required
def get_list_of_employees():
    employees_query = Employee.query.join(Job).order_by(Job.date_of_employment)
    if not employees_query:
        abort(404)
    else:
        if request.args.get('division_id'):
            employees_query = employees_query.filter(
                Job.division_id == request.args.get('division_id'))
        elif request.args.get('employment_after_date'):
            employees_query = employees_query.filter(
                Job.date_of_employment > request.args.get('employment_after_date'))
        employees = employees_query.all()
        return render_template("employees.html", name=current_user.name, list_of_employees=employees)

# @bp.route('/employee/add', methods=['POST'])
# def add_employee():
#     employee_data = {
#         "name": request.args.get('name'),
#         "surname": request.args.get('surname'),
#         "address": request.args.get('address'),
#         "patronymic": request.args.get('patronymic'),
#         "date_of_birth": request.args.get('date_of_birth')
#     }
#     try:
#         new_employee = Employee(**employee_data)
#         db.session.add(new_employee)
#         db.session.commit()
#         return new_employee
#     except Exception as ex:
#         print("error! " + str(ex))
#
#
# @bp.route('/employee/get', methods=['GET'])
# def get_employee():
#     employee = Employee.query.get(request.args.get('id'))
#
#     if not employee:
#         abort(404)
#     else:
#         print("Name of employee: ", employee.name,
#               " Surname: ", employee.surname,
#               " Patronymic: ", employee.patronymic,
#               " Address: ", employee.address,
#               " Date of birth: ", employee.date_of_birth)
#     return dict(employee)
#
#
# @bp.route('/employee/delete', methods=['DELETE'])
# def delete_employee():
#     employee = Employee.query.get(request.args.get('id'))
#
#     if not employee:
#         abort(404)
#     else:
#         db.session.delete(employee)
#         db.session.commit()
#     return 'deletion successful'
#
#
# @bp.route('/employee/edit', methods=['PUT'])
# def edit_employee():
#     employee = Employee.query.get(request.args.get('id'))
#
#     if not employee:
#         abort(404)
#     else:
#         employee.surname = request.args.get('surname')
#         db.session.add(employee)
#         db.session.commit()
#     return dict(employee)
#
#
# @bp.route('/position/add', methods=['POST'])
# def add_position():
#     position_data = {
#         "title": request.args.get('title')
#     }
#
#     try:
#         new_position = Position(**position_data)
#         db.session.add(new_position)
#         db.session.commit()
#         return new_position
#     except Exception as ex:
#         print("Error!" + str(ex))
#
#
# @bp.route('/position/get', methods=['GET'])
# def get_position():
#     position = Position.query.get(request.args.get('id'))
#
#     if not position:
#         abort(404)
#     else:
#         print("Title of position: ", position.title)
#     return dict(position)
#
#
# @bp.route('/position/delete', methods=['DELETE'])
# def delete_position():
#     position = Position.query.get(request.args.get('id'))
#
#     if not position:
#         abort(404)
#     else:
#         db.session.delete(position)
#         db.session.commit()
#     return 'deletion successful'
#
#
# @bp.route('/division/add', methods=['POST'])
# def add_division():
#     division_data = {
#         "title": request.args.get('title')
#     }
#
#     try:
#         new_division = Division(**division_data)
#         db.session.add(new_division)
#         db.session.commit()
#         return new_division
#     except Exception as ex:
#         print("Error!" + str(ex))
#
#
# @bp.route('/division/get', methods=['GET'])
# def get_division():
#     division = Division.query.get(request.args.get('id'))
#
#     if not division:
#         abort(404)
#     else:
#         print("Title of division: ", division.title)
#     return dict(division)
#
#
# @bp.route('/division/delete', methods=['DELETE'])
# def delete_division():
#     division = Division.query.get(request.args.get('id'))
#
#     if not division:
#         abort(404)
#     else:
#         db.session.delete(division)
#         db.session.commit()
#     return 'deletion successful'
#
#
# @bp.route('/employment', methods=['POST'])
# def employment():
#     employee = Employee.query.get(request.args.get('employee_id'))
#     position = Position.query.get(request.args.get('position_id'))
#     division = Division.query.get(request.args.get('division_id'))
#
#     employment_data = {
#         "staffer_id": request.args.get(employee.id),
#         "position_id": request.args.get(position.id),
#         "division_id": request.args.get(division.id),
#         "date_of_employment": request.args.get('date_of_employment')
#     }
#
#     if not employee or not position or not division:
#         abort(404)
#     else:
#         new_employment = Job(**employment_data)
#         db.session.add(new_employment)
#         db.session.commit()
#         return new_employment
#
#
# @bp.route('/dismissal', methods=['PUT'])
# def dismissal():
#     try:
#         job = Job.query.filter(Job.staffer_id == request.args.get('id')).one()
#         job.date_of_dismissal = request.args.get('date_of_dismissal')
#         db.session.add(job)
#         db.session.commit()
#         return 'employee dismissed'
#     except Exception as ex:
#         print("Error!" + str(ex))
