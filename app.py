from flask import Flask, render_template, request

app = Flask(__name__)

# ==============================
# EXPERT SYSTEM CLASSES
# ==============================

class Flight:
    def __init__(self, flight_no, destination, capacity):
        self.flight_no = flight_no
        self.destination = destination
        self.capacity = capacity
        self.remaining = capacity


class Cargo:
    def __init__(self, cargo_id, destination, weight, priority):
        self.cargo_id = cargo_id
        self.destination = destination
        self.weight = weight
        self.priority = priority
        self.assigned = False


class AirCargoExpert:

    def __init__(self):
        self.flights = []
        self.cargos = []
        self.messages = []
        self.assignments = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def add_cargo(self, cargo):
        self.cargos.append(cargo)

    def run(self):
        self.assign_high_priority()
        self.assign_low_priority()
        self.unassigned()

    def assign_high_priority(self):
        for cargo in self.cargos:
            if cargo.priority == "High" and not cargo.assigned:
                for flight in self.flights:
                    if flight.destination == cargo.destination and flight.remaining >= cargo.weight:
                        flight.remaining -= cargo.weight
                        cargo.assigned = True

                        self.messages.append(f"High Priority Cargo {cargo.cargo_id} assigned to {flight.flight_no}")

                        self.assignments.append({
                            "cargo": cargo.cargo_id,
                            "flight": flight.flight_no
                        })
                        break

    def assign_low_priority(self):
        for cargo in self.cargos:
            if cargo.priority == "Low" and not cargo.assigned:
                for flight in self.flights:
                    if flight.destination == cargo.destination and flight.remaining >= cargo.weight:
                        flight.remaining -= cargo.weight
                        cargo.assigned = True

                        self.messages.append(f"Low Priority Cargo {cargo.cargo_id} assigned to {flight.flight_no}")

                        self.assignments.append({
                            "cargo": cargo.cargo_id,
                            "flight": flight.flight_no
                        })
                        break

    def unassigned(self):
        for cargo in self.cargos:
            if not cargo.assigned:
                self.messages.append(f"Cargo {cargo.cargo_id} could not be assigned")


# ==============================
# SAMPLE DATA
# ==============================

flights = []
cargos = []

@app.route("/", methods=["GET", "POST"])
def index():

    global flights, cargos
    messages = []
    assignments = []

    if request.method == "POST":

        if "add_flight" in request.form:
            flights.append({
                "flight_no": request.form["flight_no"],
                "destination": request.form["destination"],
                "capacity": int(request.form["capacity"])
            })

        if "add_cargo" in request.form:
            cargos.append({
                "cargo_id": request.form["cargo_id"],
                "destination": request.form["cargo_destination"],
                "weight": int(request.form["weight"]),
                "priority": request.form["priority"]
            })

        if "run_system" in request.form:

            engine = AirCargoExpert()

            for f in flights:
                engine.add_flight(Flight(f["flight_no"], f["destination"], f["capacity"]))

            for c in cargos:
                engine.add_cargo(Cargo(c["cargo_id"], c["destination"], c["weight"], c["priority"]))

            engine.run()

            messages = engine.messages
            assignments = engine.assignments

    return render_template("index.html",
                           flights=flights,
                           cargos=cargos,
                           messages=messages,
                           assignments=assignments)


if __name__ == "__main__":
    app.run(debug=True)
