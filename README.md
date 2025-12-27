# 🏥 Vital Link - Comprehensive Healthcare Management Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

> **Transform the way you manage healthcare** - A modern, intuitive platform connecting patients and doctors through seamless digital experiences.

---

## 🌟 About Vital Link

**Vital Link** is a next-generation healthcare management system designed to bridge the gap between patients and medical professionals. With cutting-edge AI-powered health risk analysis, real-time appointment scheduling, and comprehensive medical record management, we're revolutionizing healthcare accessibility.

### ✨ Why Choose Vital Link?

- 🤖 **AI-Powered Diagnostics** - Advanced heart attack risk analyzer using machine learning
- 📱 **Intuitive Interface** - Beautiful, responsive design for all devices
- 🔒 **Secure & Private** - Your health data is protected with industry-standard security
- 🌍 **Location-Based Search** - Find specialized doctors near you with interactive maps
- 💬 **Community Forum** - Connect with others, ask questions, and share experiences
- 📄 **Smart OCR** - Extract text from prescription images instantly

---

## 🚀 Key Features

### For Patients

| Feature | Description |
|---------|-------------|
| **Personal Dashboard** | Centralized view of appointments, prescriptions, and medical records |
| **Heart Attack Risk Analyzer** | ML-powered tool to assess cardiovascular risk based on vital signs and lab results |
| **Appointment Scheduling** | Book appointments with doctors based on specialty and availability |
| **Medical Records** | Digital storage and access to your complete medical history |
| **Prescription Scanner** | OCR technology to digitize paper prescriptions |
| **Doctor Finder** | Location-based search with interactive maps to find nearby specialists |
| **Health Forum** | Ask questions, share experiences, and get community support |
| **Profile Management** | Update personal information and health preferences |

### For Doctors

| Feature | Description |
|---------|-------------|
| **Professional Dashboard** | Manage appointments, patient records, and consultations |
| **Patient Management** | View patient history, prescriptions, and medical records |
| **Appointment Tracking** | Real-time scheduling and appointment management |
| **Profile Showcase** | Professional profile with specialization and experience |

---

## 🎯 Project Structure

```
Arch_Hackathon/
├── 📄 HTML Pages
│   ├── index.html                    # Landing page with animations
│   ├── login.html                    # User authentication
│   ├── register.html                 # New user registration
│   ├── patient-dashboard.html        # Patient main dashboard
│   ├── doctor-dashboard.html         # Doctor main dashboard
│   ├── analyzer.html                 # Heart attack risk analyzer
│   ├── schedule-appointment.html     # Appointment booking interface
│   ├── medical_record.html           # Patient medical records viewer
│   ├── prescriptions.html            # Prescription OCR scanner
│   ├── near_by_doctor.html           # Location-based doctor search
│   ├── doctor_list.html              # Complete doctor directory
│   ├── forum.html                    # Community health forum
│   ├── services.html                 # Services overview
│   ├── about_us.html                 # About the platform
│   ├── contact.html                  # Contact information
│   ├── settings.html                 # User settings
│   └── billing.html                  # Billing and payments
│
├── 🎨 Styling
│   └── styles.css                    # Global styles and animations
│
├── 🐍 Python Scripts
│   └── generate_doctor_profiles.py   # Automated doctor profile generator
│
├── 🌐 Backend (Flask API)
│   └── env/
│       └── app.py                    # Flask server for ML predictions
│
├── 👨‍⚕️ Doctor Profiles
│   └── doctor_profiles/              # Individual doctor profile pages
│       ├── doctor1.html - doctor10.html
│
└── 📜 Documentation
    └── LICENSE                       # MIT License
```

---

## 🛠️ Technology Stack

### Frontend
- **HTML5** - Semantic markup for modern web
- **CSS3** - Advanced styling with animations and gradients
- **JavaScript (ES6+)** - Interactive functionality and dynamic content
- **Leaflet.js** - Interactive maps for doctor location
- **Tesseract.js** - Client-side OCR for prescription scanning
- **jsPDF** - PDF generation for reports

### Backend
- **Python 3.8+** - Core programming language
- **Flask 3.1.2** - Lightweight web framework
- **NumPy 2.3.4** - Numerical computing
- **Pandas 2.3.3** - Data manipulation and analysis

### Libraries & Dependencies
- **Werkzeug** - WSGI utilities
- **Jinja2** - Templating engine
- **Click** - Command-line interface
- **ItsDangerous** - Secure data signing
- **Blinker** - Signal support

---

## 📋 Prerequisites

Before running Vital Link, ensure you have the following installed:

- **Python 3.8 or higher** ([Download](https://www.python.org/downloads/))
- **pip** (Python package manager - comes with Python)
- **Modern web browser** (Chrome, Firefox, Safari, or Edge)
- **Internet connection** (for CDN resources)

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Arch_Hackathon.git
cd Arch_Hackathon
```

### Step 2: Set Up Python Virtual Environment

**On Windows:**
```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
.\env\Scripts\activate
```

**On macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv env

# Activate virtual environment
source env/bin/activate
```

### Step 3: Install Required Dependencies

```bash
pip install flask numpy pandas
```

Or if you have a requirements file:
```bash
pip install -r requirements.txt
```

### Step 4: Generate Doctor Profiles (Optional)

Run the profile generator to create sample doctor profiles:

```bash
python generate_doctor_profiles.py
```

This will create 10 doctor profile pages in the `doctor_profiles/` folder.

---

## 🎮 Running the Application

### Option 1: Run as Static Website

Simply open `index.html` in your web browser:

**Using File Explorer:**
- Navigate to the project folder
- Double-click `index.html`

**Using Command Line:**
```bash
# Windows
start index.html

# macOS
open index.html

# Linux
xdg-open index.html
```

### Option 2: Run with Flask Backend (For ML Features)

If you want to use the heart attack risk prediction API:

1. **Activate the virtual environment** (if not already activated)
2. **Navigate to the env folder:**
   ```bash
   cd env
   ```

3. **Run the Flask server:**
   ```bash
   python app.py
   ```

4. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

### Option 3: Use Python HTTP Server

For a quick local server without Flask:

```bash
python -m http.server 8000
```

Then visit: `http://localhost:8000`

---

## 📖 User Guide

### For First-Time Users

1. **Landing Page** - Start at `index.html` to explore the platform
2. **Register** - Click "Register as a New Patient" to create an account
3. **Login** - Access your dashboard with credentials
4. **Explore Features** - Navigate through:
   - Patient Dashboard for overview
   - Analyzer for health risk assessment
   - Schedule appointments with doctors
   - View medical records
   - Find nearby doctors
   - Join the community forum

### Using the Heart Attack Risk Analyzer

1. Navigate to **Analyzer** from the dashboard
2. Enter patient demographics (age, gender)
3. Input vital signs (heart rate, blood pressure)
4. Add lab results (blood sugar, CK-MB, troponin)
5. Click **"Analyze Risk"** to get AI-powered prediction
6. Download the detailed PDF report

### Finding Nearby Doctors

1. Go to **Near By Doctor** page
2. Select your required specialty
3. View doctors on the interactive map
4. Click on markers for doctor details
5. Book appointments directly

---

## 🎨 Features Showcase

### 🌈 Modern UI/UX
- **Smooth Animations** - Fade-in effects, word animations, and interactive elements
- **Gradient Backgrounds** - Eye-catching color schemes
- **Responsive Design** - Perfect on desktop, tablet, and mobile
- **Dark Mode Friendly** - Comfortable viewing in any lighting

### 🧠 AI-Powered Analysis
- Machine learning algorithms for heart attack risk prediction
- Multi-parameter health assessment
- Detailed reporting with recommendations

### 🗺️ Interactive Maps
- Real-time location detection
- Filter doctors by specialty
- Distance calculation
- Direct booking integration

---

## 🔧 Configuration

### Customizing the Application

**Change Port (Flask):**
Edit `env/app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Change port here
```

**Add More Doctors:**
Edit `generate_doctor_profiles.py` and add to the `doctors` list:
```python
doctors = [
    ("Dr. Name", "Specialty", "Years experience"),
    # Add more doctors here
]
```

**Modify Styles:**
Edit `styles.css` to customize colors, fonts, and animations.

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow existing code style and conventions
- Test your changes thoroughly
- Update documentation as needed
- Write clear commit messages

---

## 🐛 Troubleshooting

### Common Issues

**Issue:** Flask server won't start
```bash
# Solution: Make sure virtual environment is activated
.\env\Scripts\activate  # Windows
source env/bin/activate  # macOS/Linux

# Then run Flask
python env/app.py
```

**Issue:** CSS/JS not loading
- **Solution:** Check that you're opening the HTML file from a web server, not directly from the file system for certain features

**Issue:** Map not showing doctors
- **Solution:** Ensure internet connection is active (Leaflet.js requires CDN access)

**Issue:** OCR not working
- **Solution:** Check browser console for errors and ensure Tesseract.js CDN is accessible

---

## 📱 Browser Compatibility

| Browser | Supported | Notes |
|---------|-----------|-------|
| Chrome 90+ | ✅ | Fully supported |
| Firefox 88+ | ✅ | Fully supported |
| Safari 14+ | ✅ | Fully supported |
| Edge 90+ | ✅ | Fully supported |
| IE 11 | ❌ | Not supported |

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Suraj HP

---

## 👨‍💻 Author

**Suraj HP**

- GitHub: [@yourusername](https://github.com/yourusername)
- Project Link: [https://github.com/yourusername/Arch_Hackathon](https://github.com/yourusername/Arch_Hackathon)

---

## 🙏 Acknowledgments

- **Font Awesome** - Icons
- **Google Fonts** - Poppins font family
- **Leaflet.js** - Interactive mapping
- **Tesseract.js** - OCR functionality
- **jsPDF** - PDF generation
- **Flask Community** - Web framework

---

## 🌟 Star This Repository

If you find Vital Link helpful, please consider giving it a ⭐ on GitHub!

---

## 📞 Support

Having issues? Here's how to get help:

1. **Check the documentation** above
2. **Search existing issues** on GitHub
3. **Open a new issue** with detailed description
4. **Contact** via the contact page

---

<div align="center">

### Made with ❤️ for better healthcare

**Vital Link** - Connecting Health, Connecting Lives

[🏠 Home](index.html) • [📚 Documentation](#) • [🐛 Report Bug](#) • [✨ Request Feature](#)

</div>
