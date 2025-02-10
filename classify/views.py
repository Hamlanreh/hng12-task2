import requests
import math
from django.http import JsonResponse


def classify_number(request):
    number_str = request.GET.get("number")

    try:
        number = int(number_str)
    except (TypeError, ValueError):
        return JsonResponse({"error": True, "number": number_str}, status=400)

    # Determine properties
    is_prime = check_prime(number)
    is_perfect = check_perfect(number)
    is_armstrong = check_armstrong(abs(number))  # Armstrong numbers work with absolute values
    digit_sum = sum(map(int, str(abs(number))))  # Sum of digits (absolute)
    
    # Determine odd/even and Armstrong
    properties = []
    if is_armstrong:
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")

    # Get fun fact from Numbers API
    fun_fact = get_fun_fact(number)

    # Response
    return JsonResponse({
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    })

# Helper functions
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check_perfect(n):
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def check_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No fun fact available.")
    except:
        return "Could not fetch fun fact."
    return "No fun fact available."
