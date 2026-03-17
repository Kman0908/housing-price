FROM python:3.11-slim

# Install uv
RUN pip install uv

WORKDIR /app

# Copy dependency files first (for caching)
COPY requirements-app.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements-app.txt

# Copy rest of the code
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run app using uv
CMD ["uv", "run", "streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]