predictionEndpoint = "http://127.0.0.1:5000/predict"

function makePrediction() {
    fetch(predictionEndpoint, {
        credentials: "same-origin",
        mode: "same-origin",
        method: "post",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(parseForm())
    }).then(response => {
        return consumeResponse(response);
    }).then(data => {
        receivePrediction(data);
    }).catch(err => {
        if (err === "server")
            return;
        console.log(err)
    })
    return false;
}

function consumeResponse(response) {
    if (response.status === 200) {
        return response.json();
    }
    else {
        console.log("Server Status: " + response.status);
        return Promise.reject("server");
    }
}

function receivePrediction(data) {
    if (data["result"]) {
        document.getElementById("output").innerHTML = "The model suggest that your client is likely to subscribe";
    }
    else {
        document.getElementById("output").innerHTML = "The model suggest that your client is not likely to subscribe";
    }
}

function parseForm() {
    let modelInputs = {
        "age": -1,
        "job": "",
        "marital": "",
        "education": "",
        "default": "",
        "housing": "",
        "loan": "",
        "contact": "",
        "month": "",
        "day_of_week": "",
        "duration": -1,
        "campaign": -1,
        "pdays": 999,
        "previous": 0,
        "poutcome": "",
        "emp.var.rate": -1.0,
        "cons.price.idx": -1.0,
        "cons.conf.idx": -1.0,
        "euribor3m": -1.0,
        "nr.employed": -1.0
    };
    let form = document.forms["predictionForm"];
    for (let i = 0; i < form.elements.length - 1; i++) {
        let e = form.elements[i];
        let isRadio = e.getAttribute("type") === "radio";
        if (e.checked) {
            modelInputs[e.name] = e.value;
        }
        if (!isRadio) {
            modelInputs[e.name] = e.value;
        }
    }
    console.log("Form Data: ", modelInputs)
    return modelInputs;
}