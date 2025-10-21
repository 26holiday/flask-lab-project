# Static Files Directory

This directory will contain static assets (CSS, JavaScript, images).

## Planned Structure
```
static/
├── css/
│   └── style.css
├── js/
│   └── app.js
└── images/
    └── logo.png
```

## Usage
Static files are served automatically by Flask from this directory.
Access in templates using: `{{ url_for('static', filename='css/style.css') }}`
