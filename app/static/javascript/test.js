// async function get_data():

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
 }

async function get_data() {
    while (true) {
        let response = await fetch("/test");
        if (response.status != 200){
            console.log("Failed to get data")
            return ""
        }
        let result = await response.json();
        this.data = result;
        document.getElementById("data").innerText = this.data
        await sleep(16)
    }
}

get_data()