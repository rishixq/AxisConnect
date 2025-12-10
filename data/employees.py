from datetime import date

def generate_employee_data(n: int = 1):

    employee = {
        # ─────────────────────────────────────────────
        # BASIC PERSONAL DETAILS
        # ─────────────────────────────────────────────
        "employee_id": "EMP001",
        "name": "Rishi Kishore",
        "first_name": "Rishi",
        "last_name": "Kishore",
        "gender": "Male",
        "date_of_birth": "2004-02-14",
        "nationality": "Indian",
        "marital_status": "Single",
        "blood_group": "B+",
        "personal_email": "rishiexample@gmail.com",

        # ─────────────────────────────────────────────
        # CONTACT INFORMATION
        # ─────────────────────────────────────────────
        "official_email": "rishi.k@umbrella-corp.com",
        "phone_number": "98765 12345",
        "alternate_phone": "98xxx 88xxx",
        "address": {
            "line1": "No. 7, Gopalaswamy Nagar",
            "city": "Chennai",
            "state": "Tamil Nadu",
            "country": "India",
            "pincode": "600058"
        },
        "emergency_contact": {
            "name": "S Kishore Kumar",
            "relation": "Father",
            "contact_number": "98xxx 45xxx"
        },

        # ─────────────────────────────────────────────
        # CORPORATE STRUCTURE
        # ─────────────────────────────────────────────
        "designation": "Data Analyst",
        "job_level": "L3",
        "department": "Data Science",
        "sub_department": "Analytics",
        "business_unit": "AI & Engineering",
        "division": "Umbrella Corporate Services",
        "reporting_manager": "Anand Kumar",
        "manager_email": "anand.kumar@umbrella-corp.com",
        "hr_business_partner": "Priya Verma",
        "mentor": "Sanjay Rao",

        # ─────────────────────────────────────────────
        # EMPLOYMENT DETAILS
        # ─────────────────────────────────────────────
        "date_of_joining": "2024-07-01",
        "employment_type": "Full-Time",
        "contract_end_date": None,
        "probation_status": "Completed",
        "confirmation_date": "2024-12-01",
        "work_mode": "Hybrid",
        "shift_timing": "10 AM – 7 PM",
        "office_location": "Bangalore – Tech Park",
        "parking_status": "Approved",

        # ─────────────────────────────────────────────
        # ATTENDANCE & LEAVE
        # ─────────────────────────────────────────────
        "leave_balance": {
            "casual_leave": 6,
            "sick_leave": 8,
            "earned_leave": 12,
            "privilege_leave": 5,
            "comp_off": 1
        },
        "leave_history_this_year": [
            {"type": "Casual", "from": "2025-01-15", "to": "2025-01-16", "status": "Approved"},
            {"type": "Sick", "from": "2025-03-02", "to": "2025-03-02", "status": "Approved"}
        ],
        "pending_leaves": [
            {"type": "Casual", "from": "2025-12-24", "to": "2025-12-26", "status": "Pending Approval"}
        ],
        "attendance_summary": {
            "present_days": 205,
            "absent_days": 3,
            "work_from_home": 40,
            "late_marks": 2,
            "half_days": 1
        },

        # ─────────────────────────────────────────────
        # HOLIDAYS & CALENDAR
        # ─────────────────────────────────────────────
        "holidays_this_year": [
            {"date": "2025-01-01", "name": "New Year"},
            {"date": "2025-01-15", "name": "Pongal"},
            {"date": "2025-08-15", "name": "Independence Day"},
            {"date": "2025-10-02", "name": "Gandhi Jayanthi"},
            {"date": "2025-12-25", "name": "Christmas"}
        ],
        "next_holiday": {"date": "2025-12-25", "name": "Christmas"},

        # ─────────────────────────────────────────────
        # PAYROLL & FINANCE
        # ─────────────────────────────────────────────
        "current_payslip": {
            "month": "December 2025",
            "basic": 40000,
            "hra": 16000,
            "special_allowance": 8000,
            "gross": 64000,
            "pf": 1800,
            "esi": 0,
            "tax_deduction": 6000,
            "other_deductions": 1000,
            "net_pay": 55200
        },
        "ctc_breakup": {
            "yearly_ctc": 900000,
            "monthly_ctc": 75000,
            "fixed": 600000,
            "variable": 300000
        },
        "bank_account": {
            "bank_name": "HDFC Bank",
            "account_number": "xxxx5678",
            "ifsc": "HDFC0000123"
        },
        "tax_summary_this_year": {
            "financial_year": "2025-2026",
            "taxable_income": 720000,
            "tax_paid": 54000,
            "tax_slab": "10%",
            "remaining_tax": 16000,
        },

        # ─────────────────────────────────────────────
        # SKILLS & PERFORMANCE
        # ─────────────────────────────────────────────
        "skills": [
            "Python", "SQL", "Pandas", "Power BI",
            "Data Modeling", "Machine Learning Basics"
        ],
        "certifications": [
            "Google Data Analytics",
            "Azure Fundamentals",
            "Python for Data Science"
        ],
        "goals_this_year": [
            "Complete 3 analytics projects",
            "Contribute to data automation",
            "Achieve Azure Data Engineer Certificate"
        ],
        "performance_rating_last_year": "Exceeds Expectations",
        "appraisal_cycle": "Apr–Jun 2026",

        # ─────────────────────────────────────────────
        # IT & ASSET MANAGEMENT
        # ─────────────────────────────────────────────
        "assigned_assets": [
            {"item": "Dell Latitude Laptop", "asset_id": "ASSET-1029", "status": "Active"},
            {"item": "RFID Access Card", "asset_id": "CARD-8832", "status": "Active"},
            {"item": "Office Headset", "asset_id": "HS-3472", "status": "Active"}
        ],
        "pending_tickets": [
            {"ticket_id": "IT-2211", "issue": "VPN not connecting", "status": "Open"},
            {"ticket_id": "FAC-5521", "issue": "AC not working", "status": "Pending"}
        ],

        # ─────────────────────────────────────────────
        # BENEFITS & INSURANCE
        # ─────────────────────────────────────────────
        "insurance_coverage": {
            "health_insurance": "Active",
            "sum_insured": "4 Lakhs",
            "dependents": ["Mother", "Father"],
            "policy_number": "HC-99283X"
        },
        "gratuity_eligibility": True,
        "lta_balance": 10000,

        # ─────────────────────────────────────────────
        # SOCIAL & REMINDERS
        # ─────────────────────────────────────────────
        "upcoming_birthdays": [
            {"name": "Rahul Sharma", "date": "2025-12-20", "relation": "Team mate"}
        ],
        "upcoming_anniversaries": [
            {"name": "Priya Gupta", "date": "2025-12-18", "relation": "Project Manager"}
        ],

        # ─────────────────────────────────────────────
        # SECURITY & COMPLIANCE
        # ─────────────────────────────────────────────
        "id_card_status": "Active",
        "nda_signed": True,
        "data_privacy_training_completed": True,
        "security_clearance_level": "Level 2",
        "last_background_check": "2024-05-12"
    }

    return [employee]
