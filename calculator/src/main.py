import logging
import re

from flask import Flask, request
from sympy import SympifyError, sympify

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

app = Flask(__name__)

VALID_EXPRESSION_REGEX = re.compile(r"^[\d+\-*/().\s^]+$")


@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        data = request.get_json()
        expression = data.get("expression")

        if not expression or not VALID_EXPRESSION_REGEX.match(expression):
            return {
                "code": "ERROR",
                "message": "Invalid mathematical expression",
            }, 400

        result = sympify(expression)

        return {
            "code": "SUCCESS",
            "message": "Operation completed successfully",
            "result": float(result.evalf()),
        }, 200

    except SympifyError:
        return {
            "code": "ERROR",
            "message": "Invalid mathematical expression",
        }, 400
    except Exception as e:
        logger.error(f"Error evaluating expression: {e}")
        return {
            "code": "ERROR",
            "message": "An error occurred while evaluating the expression",
        }, 500
