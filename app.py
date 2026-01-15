import logging
from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)


metrics = PrometheusMetrics(app)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    """Root endpoint to verify the app is running."""
    logger.info("Home endpoint was accessed")
    return jsonify({
        "message": "Hello! The DevOps Project API is running.",
        "status": "success"
    })

@app.route('/health')
def health():
    """Health check endpoint for Kubernetes."""
    return jsonify({"status": "healthy"}), 200

@app.errorhandler(404)
def not_found(error):
    """Log 404 errors for observability."""
    logger.error(f"404 Error: Page not found - {request.path}")
    return jsonify({"error": "Resource not found"}), 404

if __name__ == '__main__':
    logger.info("Starting application on port 5000...")
    app.run(host='0.0.0.0', port=5000)