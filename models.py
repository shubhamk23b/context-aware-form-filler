{
  "fields": [
    {"key": "full_name",        "label": "Full Name",          "category": "personal",    "required": true,  "type": "text"},
    {"key": "dob",              "label": "Date of Birth",      "category": "personal",    "required": true,  "type": "date"},
    {"key": "age",              "label": "Age",                "category": "personal",    "required": true,  "type": "number"},
    {"key": "gender",           "label": "Gender",             "category": "personal",    "required": true,  "type": "text"},
    {"key": "marital_status",   "label": "Marital Status",     "category": "personal",    "required": false, "type": "text"},
    {"key": "phone",            "label": "Phone Number",       "category": "contact",     "required": true,  "type": "text"},
    {"key": "email",            "label": "Email Address",      "category": "contact",     "required": true,  "type": "email"},
    {"key": "address",          "label": "Residential Address","category": "contact",     "required": true,  "type": "textarea"},
    {"key": "city",             "label": "City",               "category": "contact",     "required": false, "type": "text"},
    {"key": "pincode",          "label": "PIN Code",           "category": "contact",     "required": false, "type": "text"},
    {"key": "aadhaar",          "label": "Aadhaar Number",     "category": "identity",    "required": true,  "type": "text"},
    {"key": "pan",              "label": "PAN Number",         "category": "identity",    "required": true,  "type": "text"},
    {"key": "occupation",       "label": "Occupation",         "category": "employment",  "required": true,  "type": "text"},
    {"key": "employer",         "label": "Employer Name",      "category": "employment",  "required": false, "type": "text"},
    {"key": "annual_income",    "label": "Annual Income (₹)",  "category": "employment",  "required": true,  "type": "number"},
    {"key": "height",           "label": "Height (cm)",        "category": "health",      "required": true,  "type": "number"},
    {"key": "weight",           "label": "Weight (kg)",        "category": "health",      "required": true,  "type": "number"},
    {"key": "smoking_status",   "label": "Smoking Status",     "category": "health",      "required": true,  "type": "text"},
    {"key": "pre_existing",     "label": "Pre-existing Conditions", "category": "health", "required": false, "type": "text"},
    {"key": "nominee_name",     "label": "Nominee Full Name",  "category": "nominee",     "required": true,  "type": "text"},
    {"key": "nominee_relation", "label": "Nominee Relation",   "category": "nominee",     "required": true,  "type": "text"},
    {"key": "nominee_dob",      "label": "Nominee Date of Birth","category": "nominee",   "required": false, "type": "date"},
    {"key": "policy_type",      "label": "Policy Type",        "category": "insurance",   "required": true,  "type": "text"},
    {"key": "coverage_amount",  "label": "Coverage Amount (₹)","category": "insurance",   "required": true,  "type": "number"},
    {"key": "policy_term",      "label": "Policy Term (years)","category": "insurance",   "required": false, "type": "number"}
  ],
  "categories": {
    "personal":   "Personal Information",
    "contact":    "Contact Information",
    "identity":   "Identity Information",
    "employment": "Employment Information",
    "health":     "Health Information",
    "nominee":    "Nominee Information",
    "insurance":  "Insurance Details"
  }
}
