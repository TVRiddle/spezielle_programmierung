Element.prototype.remove = function () {
    this.parentElement.removeChild(this);
}

function loadData() {
    loadCustomers();
    loadCars();
}

async function loadCustomers() {

    let customerSelect = document.getElementById("availableCustomers");
    customerSelect.innerHTML = "";

    let response = await fetch('https://qtp2cz8ii1.execute-api.eu-central-1.amazonaws.com/Customers', {
        method: 'POST',
        body: "{\"method\": \"customers\"}"
    });
    let result = await response.json();

    for (let i = 0; i < result.length; i++) {
        let customer = result[i];
        let option = document.createElement("option");
        let name = customer.first_name + ", " + customer.last_name;
        option.value = customer.ID;
        option.innerHTML = name;
        customerSelect.append(option);
    }

}

async function loadCars() {
    let carsSelect = document.getElementById("availableCars");
    carsSelect.innerHTML = "";
    let response = await fetch('https://qtp2cz8ii1.execute-api.eu-central-1.amazonaws.com/Cars', {
        method: 'POST',
        body: "{\"method\": \"available\"}"
    });
    let result = await response.json();
    for (let i = 0; i < result.length; i++) {
        let car = result[i];
        if (!car.is_booked) {
            let option = document.createElement("option");
            let name = car.name;
            option.value = car.ID;
            option.innerHTML = name;
            carsSelect.append(option);
        }
    }
}

async function showCars() {
    let response = await fetch('https://qtp2cz8ii1.execute-api.eu-central-1.amazonaws.com/Cars', {
        method: 'POST',
        body: "{\"method\": \"cars\"}"
    });
    let result = await response.json();
    let table = document.getElementById("cars");
    if (table.hasChildNodes()) {
        table.innerHTML = "";
    }
    let header = getHeader("cars");
    table.append(header);

    for (let i = 0; i < result.length; i++) {
        let car = result[i];
        let carElement = document.createElement('tr');
        let name = document.createElement('td');
        name.innerHTML = car.name;
        let brand = document.createElement('td');
        brand.innerHTML = car.brand;
        let color = document.createElement('td');
        color.innerHTML = car.color;
        let booked = document.createElement('td');
        booked.innerHTML = car.booked;
        let seats = document.createElement('td');
        seats.innerHTML = car.number_of_seats;
        carElement.append(name);
        carElement.append(brand);
        carElement.append(color);
        carElement.append(booked);
        carElement.append(seats);

        table.append(carElement);
    }
}

async function showCustomers() {
    let response = await fetch('https://qtp2cz8ii1.execute-api.eu-central-1.amazonaws.com/Customers', {
        method: 'POST',
        body: "{\"method\": \"customers\"}"
    });
    let result = await response.json();

    let table = document.getElementById("customers");
    if (table.hasChildNodes()) {
        table.innerHTML = "";
    }
    let header = getHeader("customers");
    table.append(header);

    for (let i = 0; i < result.length; i++) {
        let customer = result[i];
        let customerElement = document.createElement('tr');
        let vorname = document.createElement('td');
        vorname.innerHTML = customer.first_name;
        let nachname = document.createElement('td');
        nachname.innerHTML = customer.last_name;
        let tdHistoryButton = document.createElement('td');
        let historyButton = document.createElement('button');
        historyButton.innerHTML = "show history";
        historyButton.classList = "btn btn-info";
        historyButton.setAttribute("data-id", customer.ID);

        historyButton.addEventListener("click", toggleHistory)
        historyButton.tagName = "historyButton"
        tdHistoryButton.append(historyButton);

        customerElement.append(vorname);
        customerElement.append(nachname);
        customerElement.append(tdHistoryButton);

        table.append(customerElement);
    }
}

function toggleHistory() {

    if (this.innerHTML == "hide history") {
        hideHistory(this);
        this.innerHTML = "show history";
    } else {
        showHistory(this);
        this.innerHTML = "hide history";
    }

    function hideHistory(button) {
        let customer = button.parentElement.parentElement;
        let index = getIndexOfElement(customer) + 1;
        let toRemove = customer.parentElement.childNodes.item(index);
        customer.parentElement.removeChild(toRemove);
    }

    async function showHistory(button) {
        let customer_id = button.getAttribute("data-id");

        let response = await fetch('https://qtp2cz8ii1.execute-api.eu-central-1.amazonaws.com/Customers', {
            method: 'POST',
            body: "{\"method\": \"history\",\"customer_id\": " + customer_id + "}"
        });
        let result = await response.json();

        let newTable = document.createElement("table");
        newTable.classList = "table-dark";
        let header = getHeader("history");
        newTable.append(header);
        for (let i = 0; i < result.length; i++) {
            let history = result[i];
            let historyElement = document.createElement('tr');
            let carName = document.createElement('td');
            carName.innerHTML = history.car_name;
            let start = document.createElement('td');
            start.innerHTML = new Date(history.start * 1000);
            let end = document.createElement('td');
            end.innerHTML = new Date(history.end * 1000);

            historyElement.append(carName);
            historyElement.append(start);
            historyElement.append(end);

            newTable.append(historyElement);
        }

        let newTableRow = document.createElement('tr');
        let newTableData = document.createElement('td');
        newTableData.id = "historyTable";
        newTableData.setAttribute("colspan", "3");
        newTableData.append(newTable)
        newTableRow.append(newTableData);
        button.parentElement.parentElement.parentElement.insertBefore(newTableRow, button.parentElement.parentElement.nextSibling);
    }
}

async function book() {
    let customer_id = document.getElementById("availableCustomers").value;
    let car_id = document.getElementById("availableCars").value;

    let response = await fetch('https://qtp2cz8ii1.execute-api.eu-central-1.amazonaws.com/Bookings', {
        method: 'POST',
        body: "{\"method\": \"book\",\"customer_id\": " + customer_id + ",\"car_id\": " + car_id + "}"
    });
    let result = await response.json();

    if (result['success'] == "true") {
        alert("Juhu Buchung vorgenommen ;)");
    } else {
        alert("Que pena eres tu! Ahora se te jaman Carlos");
    }
    loadData();
}

function getHeader(kind) {
    let header = document.createElement("tr");
    switch (kind) {
        case "cars":
            let nameHeader = document.createElement("th");
            nameHeader.innerHTML = "Name";
            let brandHeader = document.createElement("th");
            brandHeader.innerHTML = "Marke";
            let colorHeader = document.createElement("th");
            colorHeader.innerHTML = "Farbe";
            let bookedHeader = document.createElement("th");
            bookedHeader.innerHTML = "Gebucht";
            let seatsHeader = document.createElement("th");
            seatsHeader.innerHTML = "Anzahl Sitze";
            header.append(nameHeader);
            header.append(brandHeader);
            header.append(colorHeader);
            header.append(bookedHeader);
            header.append(seatsHeader);
            break;
        case "customers":
            let firstNameHeader = document.createElement("th");
            firstNameHeader.innerHTML = "Vorname";
            let lastNameHeader = document.createElement("th");
            lastNameHeader.innerHTML = "Nachname";
            let historyHeader = document.createElement("th");
            historyHeader.innerHTML = "Buchungshistorie";
            header.append(firstNameHeader);
            header.append(lastNameHeader);
            header.append(historyHeader);
            break;
        case "history":
            let carName = document.createElement("th");
            carName.innerHTML = "Autotyp";
            let start = document.createElement("th");
            start.innerHTML = "Start";
            let end = document.createElement("th");
            end.innerHTML = "Ende";
            header.append(carName);
            header.append(start);
            header.append(end);
            break;
    }
    return header;
}

function getIndexOfElement(el) {
    var children = el.parentNode.childNodes,
        i = 0;
    for (; i < children.length; i++) {
        if (children[i] == el) {
            return i;
        }
    }
    return -1;
}