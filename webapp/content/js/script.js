function httpGet(url) {
    console.log("Send request to -> " + url);
    let xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, false);
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

function showCustomers() {
    let result = JSON.parse(httpGet("/api/customers"));
    let table = document.getElementById("customers");
    table.innerHTML = "";
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
        historyButton.setAttribute("data-id", customer.first_name + "," + customer.last_name);
        historyButton.addEventListener("click", showHistory)
        tdHistoryButton.append(historyButton);

        customerElement.append(vorname);
        customerElement.append(nachname);
        customerElement.append(tdHistoryButton);

        table.append(customerElement);
    }
}

function showHistory() {
    // todo hide again
    let firstName = this.getAttribute("data-id").split(",")[0];
    let lastName = this.getAttribute("data-id").split(",")[1];

    let result = JSON.parse(httpGet("/api/customer/" + firstName + "/" + lastName + "/history"));

    let newTable = document.createElement("table");
    newTable.classList = "table-dark";
    let header = getHeader("history");
    newTable.append(header);
    for (let i = 0; i < result.length; i++) {
        let history = result[i];
        console.log(history);
        let historyElement = document.createElement('tr');
        let carName = document.createElement('td');
        carName.innerHTML = history.car_name;
        let start = document.createElement('td');
        start.innerHTML = history.start;
        let end = document.createElement('td');
        end.innerHTML = history.end;

        historyElement.append(carName);
        historyElement.append(start);
        historyElement.append(end);

        newTable.append(historyElement);
    }

    let newTableRow = document.createElement('tr');
    let newTableData = document.createElement('td');
    newTableData.setAttribute("colspan", "3");
    newTableData.append(newTable)
    newTableRow.append(newTableData);
    this.parentElement.parentElement.parentElement.insertBefore(newTableRow, this.parentElement.parentElement.nextSibling);
}

function showCars() {
    let result = JSON.parse(httpGet("/api/cars"));
    let table = document.getElementById("cars");
    table.innerHTML = "";
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

function book() {
    let customer = document.getElementById("availableCustomers").value;
    let firstName = customer.split(",")[0];
    let lastName = customer.split(",")[1];
    let car = document.getElementById("availableCars").value;

    let result = httpGet("/api/customer/" + firstName + "/" + lastName + "/book/" + car);

    if (result=="true") {
        alert("Juhu Buchung vorgenommen ;)");
    } else {
        alert("Que pena eres tu! Ahora se te jaman Carlos");
    }
    loadData();
}

function loadData() {
    // Load customers
    let customerSelect = document.getElementById("availableCustomers");
    customerSelect.innerHTML = "";
    let result = JSON.parse(httpGet("/api/customers"));

    for (let i = 0; i < result.length; i++) {
        let customer = result[i];
        let option = document.createElement("option");
        let name = customer.first_name + "," + customer.last_name;
        option.value = name;
        option.innerHTML = name;
        customerSelect.append(option);
    }

    // Load free cars
    let carsSelect = document.getElementById("availableCars");
    carsSelect.innerHTML = "";
    result = JSON.parse(httpGet("/api/cars"));
    for (let i = 0; i < result.length; i++) {
        let car = result[i];
        if (!car.is_booked) {
            let option = document.createElement("option");
            let name = car.name;
            option.value = name;
            option.innerHTML = name;
            carsSelect.append(option);
        }
    }
}