import os
import sys

# Attempt to make stdout use utf-8 (works on Python 3.7+)
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    # ignore if not supported (older Python) — we'll still avoid emojis below
    pass

# Folder where profiles will be saved
output_folder = "doctor_profiles"
os.makedirs(output_folder, exist_ok=True)

# Doctor data
doctors = [
    ("Dr. Rahul Mehta", "Cardiologist", "12 yrs experience"),
    ("Dr. Aisha Kapoor", "Neurologist", "10 yrs experience"),
    ("Dr. Sameer Verma", "Orthopedic Surgeon", "9 yrs experience"),
    ("Dr. Nisha Reddy", "Pediatrician", "8 yrs experience"),
    ("Dr. Arjun Singh", "General Physician", "11 yrs experience"),
    ("Dr. Sneha Das", "Dermatologist", "7 yrs experience"),
    ("Dr. Vivek Sharma", "Oncologist", "15 yrs experience"),
    ("Dr. Priya Menon", "Gynecologist", "10 yrs experience"),
    ("Dr. Karan Bhatt", "Psychiatrist", "9 yrs experience"),
    ("Dr. Meera Nair", "Endocrinologist", "13 yrs experience"),
]

# HTML template for doctor profile page
template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{name} | Vital Link</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap" rel="stylesheet">
<style>
body {{
  font-family: 'Poppins', sans-serif;
  background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
  color: #fff;
  margin: 0;
  padding: 0;
  text-align: center;
  -webkit-font-smoothing: antialiased;
}}
header {{
  padding: 80px 20px 40px;
  animation: fadeInDown 1.2s ease;
}}
header h1 {{
  font-size: 42px;
  font-weight: 800;
  color: #00e0ff;
  margin: 0;
}}
p.speciality {{
  font-size: 1.3rem;
  color: #bfeefc;
  margin: 10px 0;
}}
p.exp {{
  color: #d7eef6;
  font-size: 1.1rem;
  margin-bottom: 30px;
}}
.profile-container {{
  max-width: 800px;
  margin: 0 auto;
  background: rgba(255,255,255,0.06);
  padding: 40px 20px;
  border-radius: 16px;
  box-shadow: 0 8px 25px rgba(0,0,0,0.25);
  animation: fadeInUp 1.4s ease;
}}
img.photo {{
  width: 180px;
  height: 180px;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid #00e0ff;
  box-shadow: 0 0 20px rgba(0,224,255,0.25);
}}
a.back-btn {{
  display: inline-block;
  margin-top: 28px;
  padding: 10px 26px;
  text-decoration: none;
  background: linear-gradient(90deg, #00e0ff, #4de1ff);
  color: #072027;
  border-radius: 999px;
  font-weight: 700;
  transition: 0.25s;
}}
a.back-btn:hover {{
  transform: translateY(-3px);
  box-shadow: 0 12px 32px rgba(0,224,255,0.25);
}}
footer {{
  text-align: center;
  padding: 30px 0;
  color: #dfeff4;
  margin-top: 50px;
  font-size: 0.95rem;
}}
@keyframes fadeInDown {{
  from {{opacity: 0; transform: translateY(-36px);}}
  to {{opacity: 1; transform: translateY(0);}}
}}
@keyframes fadeInUp {{
  from {{opacity: 0; transform: translateY(36px);}}
  to {{opacity: 1; transform: translateY(0);}}
}}
</style>
</head>
<body>
<header>
  <img class="photo" src="https://randomuser.me/api/portraits/{gender}/{photo_id}.jpg" alt="{name}">
  <h1>{name}</h1>
  <p class="speciality">{speciality}</p>
  <p class="exp">{experience}</p>
</header>
<div class="profile-container">
  <p><strong>{name}</strong> is a highly skilled {speciality_lower} with {experience_lower} in providing compassionate and expert care to patients.</p>
  <p>Proudly working under <strong>Vital Link Healthcare</strong>, {first_name} is dedicated to advancing patient well-being using the latest medical innovations and personalized care.</p>
  <p><strong>Contact:</strong><br>Email: {email}<br>Phone: +91-{phone}</p>
  <a class="back-btn" href="../doctorlist.html">← Back to Doctors</a>
</div>
<footer>
  © 2025 Vital Link Healthcare — Empowering Wellness with Innovation
</footer>
</body>
</html>
"""

# Generate HTML files
for i, (name, speciality, exp) in enumerate(doctors, start=1):
    # Determine gender for randomuser API
    first_name = name.split()[1]
    female_names = ["Aisha", "Nisha", "Sneha", "Priya", "Meera"]
    gender = "women" if any(f == first_name for f in female_names) else "men"
    photo_id = 20 + i

    # Contact details
    email = f"{name.lower().replace(' ','.')}@vitallink.com"
    phone = f"9{i}23{i}45{i}6"

    # Render HTML
    html_content = template.format(
        name=name,
        speciality=speciality,
        experience=exp,
        speciality_lower=speciality.lower(),
        experience_lower=exp.lower(),
        first_name=first_name,
        gender=gender,
        photo_id=photo_id,
        email=email,
        phone=phone
    )

    # Write to file
    file_path = os.path.join(output_folder, f"doctor{i}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

# Use plain ASCII text in the final print to avoid console encoding issues
print("Successfully generated {} doctor profile pages inside '{}/'.".format(len(doctors), output_folder))
