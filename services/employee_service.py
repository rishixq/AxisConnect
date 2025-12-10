from sqlalchemy.orm import Session
from models import Employee, EmployeeSalary, LeaveRecord, SkillRecord, GoalRecord, AssetRecord

# -----------------------------------------------------------
# FETCH EMPLOYEE BY CODE OR EMAIL
# -----------------------------------------------------------
def get_employee_by_code(db: Session, employee_code: str):
    return db.query(Employee).filter(Employee.employee_code == employee_code).first()


# -----------------------------------------------------------
# FULL EMPLOYEE PROFILE AS A CLEAN PYTHON DICT
# -----------------------------------------------------------
def get_full_employee_profile(db: Session, employee_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return None

    salary = db.query(EmployeeSalary).filter(EmployeeSalary.employee_id == employee_id).first()
    leaves = db.query(LeaveRecord).filter(LeaveRecord.employee_id == employee_id).all()
    skills = db.query(SkillRecord).filter(SkillRecord.employee_id == employee_id).all()
    goals = db.query(GoalRecord).filter(GoalRecord.employee_id == employee_id).all()
    assets = db.query(AssetRecord).filter(AssetRecord.employee_id == employee_id).all()

    return {
        "employee_code": employee.employee_code,
        "name": employee.name,
        "email": employee.email,
        "phone": employee.phone,
        "gender": employee.gender,
        "dob": str(employee.date_of_birth),
        "role": employee.role,
        "department": employee.department,
        "location": employee.location,
        "job_level": employee.job_level,
        "join_date": str(employee.join_date),
        "employment_type": employee.employment_type,
        "emergency_contact": employee.emergency_contact,
        "address": employee.address,

        "salary": {
            "ctc": salary.ctc if salary else None,
            "basic_pay": salary.basic_pay if salary else None,
            "hra": salary.hra if salary else None,
            "pf": salary.pf if salary else None,
            "esi": salary.esi if salary else None,
            "tax_deduction": salary.tax_deduction if salary else None
        },

        "skills": [
            {
                "skill_name": s.skill_name,
                "experience_years": s.experience_years,
                "certification": s.certification
            } for s in skills
        ],

        "goals": [
            {
                "goal_title": g.goal_title,
                "description": g.description,
                "due_date": str(g.due_date),
                "status": g.status
            } for g in goals
        ],

        "assets": [
            {
                "asset_type": a.asset_type,
                "serial_number": a.serial_number,
                "issue_date": str(a.issue_date),
                "status": a.status
            } for a in assets
        ],

        "leave_history": [
            {
                "leave_type": l.leave_type,
                "start_date": str(l.start_date),
                "end_date": str(l.end_date),
                "status": l.status
            } for l in leaves
        ]
    }
