# 🎨 Open edX Purple and White Theme Plugin

A custom Tutor plugin designed to apply consistent **Purple and White branding** across Open edX LMS, Studio (CMS), and Learning MFE using the Indigo theme.

## 📌 Project Overview

This project provides centralized theme customization for the Open edX platform through a custom Tutor plugin.

It uses Tutor plugin hooks to integrate custom SCSS theme variables and inject CSS into the Learning MFE during the Docker build process.

The goal is to provide a consistent visual identity across the different Open edX interfaces while maintaining the existing Indigo theme structure.

## 🎨 Theme Colour Palette

| Colour | Hex Code | Purpose |
|---|---|---|
| Primary Purple | `#6C3FC5` | Primary branding and buttons |
| Light Purple | `#F0EAFB` | Secondary backgrounds |
| Dark Purple | `#492878` | Hover and darker elements |
| White | `#FFFFFF` | Text and backgrounds |

## ✨ Key Features

### 1. LMS (Learning Management System)
- Custom purple primary theme colour.
- Light purple theme variables.
- Custom typography variables.
- Integration with the Indigo theme.

### 2. Studio / CMS (Course Authoring)
- Purple primary and secondary theme variables.
- Purple Studio action buttons.
- Darker purple hover and focus states.
- Custom typography variables.

### 3. Learning MFE (Micro-Frontend)
- Purple navigation hover and active states.
- Purple navigation tab indicators.
- Purple sequence navigation indicators.
- Purple branding links.
- Purple primary banners.

## 🛠️ Technology Stack

- **Platform:** Open edX
- **Plugin Framework:** Tutor
- **Programming Language:** Python
- **Styling:** SCSS and CSS
- **Containerization:** Docker
- **Base Theme:** Indigo

## 📂 Project Structure

```text
openedx-purple-white-theme/
│
├── .gitignore
├── README.md
│
└── tutor-theme/
    ├── pyproject.toml
    │
    └── tutortheme/
        ├── __init__.py
        ├── plugin.py
        │
        └── templates/
            └── indigo/
                ├── lms/
                │   └── static/sass/partials/lms/theme/
                │       └── _variables.scss
                │
                └── cms/
                    └── static/sass/partials/cms/theme/
                        └── _variables.scss
```

## ⚙️ Installation and Setup

### Prerequisites

- Python
- Tutor 19.x
- Docker
- Open edX Sumac 1 environment

### Step 1: Clone the Repository

```bash
git clone https://github.com/apeksha-code-maker/openedx-purple-white-theme.git

cd openedx-purple-white-theme
```

### Step 2: Install the Plugin

From the project root directory:

```bash
pip install -e ./tutor-theme
```

### Step 3: Enable the Tutor Plugin

```bash
tutor plugins enable openedxtheme
```

### Step 4: Save Configuration and Build Images

```bash
tutor config save

tutor images build openedx

tutor images build mfe
```

### Step 5: Apply the Indigo Theme

```bash
tutor local do settheme indigo
```

### Step 6: Start Open edX Services

```bash
tutor local start lms cms mfe -d
```

**Note:** Use the appropriate Tutor environment and configuration for your Open edX installation.

## 🔧 Plugin Configuration

The plugin is registered through the Tutor plugin entry point:

```toml
[project.entry-points."tutor.plugin.v1"]
openedxtheme = "tutortheme.plugin"
```

The plugin uses Tutor hooks to:

- Register custom theme template directories.
- Copy Indigo theme customizations into the Open edX theme directory.
- Include custom LMS and CMS SCSS files.
- Inject Purple and White CSS into the Learning MFE during its Docker build.

## 🧪 Tested Environment

| Component | Version |
|---|---|
| Tutor | 19.0.1 |
| Open edX Release | Sumac 1 |
| Base Theme | Indigo |
| MFE Image | 19.0.1-indigo |

## 📜 License

This project declares the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

## 👩‍💻 Repository

**GitHub:** https://github.com/apeksha-code-maker/openedx-purple-white-theme

---

*Developed to provide consistent Purple and White branding across the Open edX learning platform.*
