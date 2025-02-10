# 📊 Number Classification API

This API takes a number as input and returns its mathematical properties, including whether it is prime, perfect, Armstrong, odd/even, and its digit sum. It also provides a fun fact about the number using the [Numbers API](http://numbersapi.com/). 🚀

---

## 🌟 Features

✅ Classifies a number as **prime, perfect, Armstrong, odd, or even**  
✅ Returns the **sum of the digits**  
✅ Fetches a **fun fact** about the number from an external API  
✅ Returns responses in **JSON format**  
✅ Handles **input validation and errors**  
✅ **Fast & lightweight** API  

---

## 📖 API Documentation

### **1️⃣ Endpoint**

```http
GET https://hng12-task2-ozst.onrender.com/api/classify-number?number=<integer>
```

### **2️⃣ Example Request**

```
GET https://hng12-task2-ozst.onrender.com/api/classify-number?number=371
```

### **3️⃣ Example Response (200 OK)**

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### **4️⃣ Error Response (400 Bad Request)**

```json
{
    "error": true,
    "number": "alphabet"
}
```

---

## 🛠️ Local Setup & Installation

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/Hamlanreh/hng12-task2.git
cd hng12-task2
```

### **2️⃣ Install Dependencies**

```sh
pip install -r requirements.txt
```

### **3️⃣ Run Migrations**

```sh
python manage.py migrate
```

### **4️⃣ Start the Django Server**

```sh
python manage.py runserver
```

🚀 The API will be available at:
```
http://127.0.0.1:8000/api/classify-number?number=371
```

---

## 🌍 Deployment

This API is deployed on **Render** and is publicly accessible at:

🔗 **Live API URL:**  
```
https://hng12-task2-ozst.onrender.com/api/classify-number?number=371
```

---

## 🏗️ Built With

- **Python** 🐍
- **Django REST Framework** ⚡
- **Render (Hosting)** 🌍
- **Numbers API (Fun Fact)** 🎲

---

## 💡 How It Works

1. The API accepts a **GET request** with a `number` parameter.
2. It checks if the number is **prime, perfect, Armstrong, odd, or even**.
3. It calculates the **sum of the digits**.
4. It fetches a **fun fact** from [Numbers API](http://numbersapi.com/).
5. It returns a **JSON response**.

---

## 🚀 Future Improvements

- 🛠️ Add more number properties (e.g., Fibonacci, palindromes)
- 📊 Include graphical data visualization for numbers
- 📝 Improve error handling and API performance