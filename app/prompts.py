def prompts():
  return [
    {"key":"Primary Care Visit to Treat an Injury or Illness", "questions": [
      "What is the primary care visit cost or percentage for plan provider",
      "What is the primary care visit cost or percentage for non-plan provider",
    ]},
    {"key":"Specialist Visit", "questions": [
      "What is the Specialist Visit cost or percentage for plan provider",
      "What is the Specialist Visit cost or percentage for non-plan provider"
    ]},
    {"key":"Other Practitioner Office Visit (Nurse, Physician Assistant)", "questions": []},
    {"key":"Outpatient Facility Fee (e.g., Ambulatory Surgery Center)", "questions": [
      "What is the ambulatory surgery center cost or percentage for plan provider",
      "What is the ambulatory surgery center cost or percentage for non-plan provider"
    ]},
    {"key":"Outpatient Surgery Physician/Surgical Services", "questions": [
      "What is the Physician/surgeon cost or percentage for plan provider",
      "What is the Physician/surgeon cost or percentage for non-plan provider"
    ]},
    {"key":"Hospice Services", "questions": [
      "What is the Hospice service cost or percentage for plan provider",
      "What is the Hospice service cost or percentage for non-plan provider"
    ]},
    {"key":"Urgent Care Centers or Facilities", "questions": [
      "What is the Urgent care cost or percentage for plan provider",
      "What is the Urgent care cost or percentage for non-plan provider"
    ]},
    {"key":"Home Health Care Services", "questions": [
      "What is the Home health care cost or percentage for plan provider",
      "What is the Home health care cost or percentage for non-plan provider"
    ]},
    {"key":"Emergency Room Services", "questions": [
      "What is the Emergency room care cost or percentage for plan provider",
      "What is the Emergency room care cost or percentage for non-plan provider"
    ]},
    {"key":"Emergency Transportation/Ambulance", "questions": [
      "What is the Emergency medical transportation cost or percentage for plan provider",
      "What is the Emergency medical transportation cost or percentage for non-plan provider"
    ]},
    {"key":"Inpatient Hospital Services (e.g., Hospital Stay)", "questions": [
      "What is the Facility fee (e.g.,hospital room) cost or percentage for plan provider",
      "What is the Facility fee (e.g.,hospital room) cost or percentage for non-plan provider"
    ]},
    {"key":"Inpatient Physician and Surgical Services", "questions": []},
    {"key":"Skilled Nursing Facility", "questions": [
      "What is the Skilled nursing care cost or percentage for plan provider",
      "What is the Skilled nursing care cost or percentage for non-plan provider"
    ]},
    {"key":"Prenatal and Postnatal Care", "questions": [
      "What is the Childbirth/delivery professional services cost or percentage for plan provider",
      "What is the Childbirth/delivery professional services cost or percentage for non-plan provider"
    ]},
    {"key":"Delivery and All Inpatient Services for Maternity Care", "questions": [
      "What is the Childbirth/delivery facility services cost or percentage for plan provider",
      "What is the Childbirth/delivery facility services cost or percentage for non-plan provider"
    ]},
    {"key":"Mental/Behavioral Health Outpatient Services", "questions": [
      "What is the metal health Outpatient services cost or percentage for plan provider",
      "What is the metal health Outpatient services cost or percentage for non-plan provider"
    ]},
    {"key":"Mental/Behavioral Health Inpatient Services", "questions": [
      "What is the metal health Inpatient services cost or percentage for plan provider",
      "What is the metal health Inpatient services cost or percentage for non-plan provider"
    ]},
    {"key":"Substance Abuse Disorder Outpatient Services", "questions": []},
    {"key":"Substance Abuse Disorder Inpatient Services", "questions": []},
    {"key":"Generic Drugs", "questions": [
      "What is the generic drugs cost or percentage for plan provider",
      "What is the generic drugs cost or percentage for non-plan provider"
    ]},
    {"key":"Preferred Brand Drugs", "questions": [
      "What is the Preferred Brand drugs cost or percentage for plan provider",
      "What is the Preferred Brand drugs cost or percentage for non-plan provider"
    ]},
    {"key":"Non-Preferred Brand Drugs", "questions": [
      "What is the Non-Preferred Brand drugs cost or percentage for plan provider",
      "What is the Non-Preferred Brand drugs cost or percentage for non-plan provider"
    ]},
    {"key":"Specialty Drugs", "questions": [
      "What is the Specialty Drugs cost or percentage for plan provider",
      "What is the Specialty Drugs cost or percentage for non-plan provider"
    ]},
    {"key":"Outpatient Rehabilitation Services", "questions": [
      "What is the Rehabilitation services outpatient cost or percentage for plan provider",
      "What is the Rehabilitation services outpatient cost or percentage for non-plan provider"
    ]},
    {"key":"Chiropractic Care", "questions": []},
    {"key":"Durable Medical Equipment", "questions": [
      "What is the Durable Medical Equipment cost or percentage for plan provider",
      "What is the Durable Medical Equipment cost or percentage for non-plan provider"
    ]},
    {"key":"Imaging (CT/PET Scans, MRIs)", "questions": [
      "What is the Imaging (CT/PET scans, MRI's) cost or percentage for plan provider",
      "What is the Imaging (CT/PET scans, MRI's) cost or percentage for non-plan provider"
    ]},
    {"key":"Preventive Care/Screening/Immunization", "questions": [
      "What is the Preventive care/screening/immunization cost or percentage for plan provider",
      "What is the Preventive care/screening/immunization cost or percentage for non-plan provider"
    ]},
    {"key":"Acupuncture", "questions": []},
    {"key":"Routine Eye Exam for Children", "questions": [
      "What is the Children's eye exam cost or percentage for plan provider",
      "What is the Children's eye exam cost or percentage for non-plan provider"
    ]},
    {"key":"Eye Glasses for Children", "questions": [
      "What is the Children's glasses cost or percentage for plan provider",
      "What is the Children's glasses cost or percentage for non-plan provider"
    ]},
    {"key":"Dental Check-Up for Children", "questions": [
      "What is the Children's dental check-up cost or percentage for plan provider",
      "What is the Children's dental check-up cost or percentage for non-plan provider"
    ]},
    {"key":"Rehabilitative Speech Therapy", "questions": [
      "What is the Rehabilitation services inpatient cost or percentage for plan provider",
      "What is the Rehabilitation services inpatient cost or percentage for non-plan provider"
    ]},
    {"key":"Rehabilitative Occupational and Rehabilitative Physical Therapy", "questions": []},
    {"key":"Well Baby Visits and Care", "questions": []},
    {"key":"Laboratory Outpatient and Professional Services", "questions": [
      "What is the Diagnostic test (x-ray, blood work) cost or percentage for plan provider",
      "What is the Diagnostic test (x-ray, blood work) cost or percentage for non-plan provider"
    ]},
    {"key":"X-rays and Diagnostic Imaging", "questions": []},
    {"key":"Basic Dental Care - Child", "questions": []},
    {"key":"Orthodontia - Child", "questions": []},
    {"key":"Major Dental Care - Child", "questions": []},
    {"key":"Abortion for Which Public Funding is Prohibited", "questions": [
        "What is the termination of pregnancy cost or percentage for plan provider"
    ]},
    {"key":"Transplant", "questions": [
        "What is the Hospital Inpatient Care Physician and surgical Services cost or percentage for plan provider"
    ]},
    {"key":"Accidental Dental", "questions": []},
    {"key":"Dialysis", "questions": [
        "What is the Dialysis Services Outpatient Care cost or percentage for plan provider"
    ]},
    {"key":"Allergy Testing", "questions": [
        "What is the Allergy Services Evaluation and treatment cost or percentage for plan provider"
    ]},
    {"key":"Chemotherapy", "questions": []},
    {"key":"Radiation", "questions": []},
    {"key":"Diabetes Education", "questions": []},
    {"key":"Diabetes Education", "questions": []},
    {"key":"Infusion Therapy", "questions": []},
    {"key":"Treatment for Temporomandibular Joint Disorders", "questions": []},
    {"key":"Nutritional Counseling", "questions": [
        "What is the Medical Nutrition Therapy & Counseling cost or percentage for plan provider"
    ]},
    {"key":"Reconstructive Surgery", "questions": [
      "What is the Reconstructive Surgery cost or percentage for plan provider"
    ]},
  ]
  