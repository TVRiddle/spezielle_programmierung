Element.prototype.remove = function () {
    this.parentElement.removeChild(this);
}

function loadData() {
    // Load customers
    let customerSelect = document.getElementById("availableCustomers");
    customerSelect.innerHTML = "";
    let result = JSON.parse(httpGet("/api/customers"));

    for (let i = 0; i < result.length; i++) {
        let customer = result[i];
        console.log(customer)
        let option = document.createElement("option");
        let name = customer.first_name + ", " + customer.last_name;
        option.value = customer._id.$oid;
        option.innerHTML = name;
        customerSelect.append(option);
    }

    // Load free cars
    let carsSelect = document.getElementById("availableCars");
    carsSelect.innerHTML = "";
    result = JSON.parse(httpGet("/api/cars/available"));
    for (let i = 0; i < result.length; i++) {
        let car = result[i];
        console.log(car)
        if (!car.is_booked) {
            let option = document.createElement("option");
            let name = car.name;
            option.value = car._id.$oid;
            option.innerHTML = name;
            carsSelect.append(option);
        }
    }
}

function showCars() {
    let result = JSON.parse(httpGet("/api/cars"));
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
        booked.innerHTML = car.is_booked;
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

function showCustomers() {
    let result = JSON.parse(httpGet("/api/customers"));

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
        historyButton.setAttribute("data-id", customer._id.$oid);

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

    function showHistory(button) {
        let customer_id = button.getAttribute("data-id");

        let result = JSON.parse(httpGet("/api/customer/" + customer_id + "/history"));

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

function book() {
    let customer_id = document.getElementById("availableCustomers").value;
    let car_id = document.getElementById("availableCars").value;

    let result = httpGet("/api/customer/" + customer_id + "/book/" + car_id);

    if (result == "true") {
        alert("Juhu Buchung vorgenommen ;)");
    } else {
        alert("Que pena eres tu! Ahora se te jaman Carlos");
    }
    loadData();
}

function httpGet(url) {
    console.log("Send request to -> " + url);
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, false);
    xmlHttp.send(null);
    return xmlHttp.responseText;
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