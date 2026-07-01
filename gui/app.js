async function test() {

    const response = await fetch(
        '/api'
    );

    const data = await response.json();

    document.getElementById("result")
        .innerHTML =
        JSON.stringify(data, null, 2);
}