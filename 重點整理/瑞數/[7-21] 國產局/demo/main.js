require("./env")
require("./ts")
require("./auto")


function get_cookie() {
    return document.cookie
}

console.log(get_cookie())