# ✈️ AirCargo Expert System (Flask)

An **AI-based Expert System for Airline Cargo Scheduling** built using **Python Flask**.
This system helps assign cargo to flights based on **destination, capacity, and priority** using rule-based reasoning.

---

##  Features

* Add flights with destination and capacity
* Add cargo with weight and priority
* Automatic cargo assignment to flights
* Priority-based scheduling (High / Low)
* Detect unassigned cargo due to capacity or missing flights
* Simple web interface using **Flask, HTML, and CSS**

---

## 🧠 Expert System Rules

The system uses **rule-based inference**:

1. **High Priority Rule**

   * High priority cargo is assigned first to available flights.

2. **Low Priority Rule**

   * Low priority cargo is assigned after high priority cargo.

3. **Unassigned Cargo Rule**

   * If no flight is available or capacity is insufficient, cargo remains unassigned.


## ⚙️ Technologies Used

* **Python**
* **Flask**
* **HTML**
* **CSS**
* **Rule-Based Expert System**

--


## 📊 Example

Flights:

```
AI101 → Delhi → 500kg
AI202 → Mumbai → 300kg
```

Cargo:

```
C001 → Delhi → 150kg → High
C002 → Mumbai → 100kg → Low
```

The system automatically assigns cargo to suitable flights.

---




