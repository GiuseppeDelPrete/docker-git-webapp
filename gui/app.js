async function test() {

    const response = await fetch(
        'http://localhost:5000/api'
    );

    const data = await response.json();

    document.getElementById("result")
        .innerHTML =
        JSON.stringify(data, null, 2);
}