#!/usr/bin/env python3
"""
WSGI entry point for Rivaq Engineering Consultancy Management System
"""

import os
import sys

# Add the application directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app

# Create the Flask application
app = create_app()

if __name__ == "__main__":
    # For development only
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

