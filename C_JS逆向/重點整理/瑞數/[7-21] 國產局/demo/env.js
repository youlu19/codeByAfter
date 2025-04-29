content = "metaContent"


window = top = self = global

window.addEventListener = function () {
}
window.attachEvent = function () {
}

div = {
    getElementsByTagName() {
        return []
    }
}
head = {
    removeChild() {

    }
}
script = {
    getAttribute(attr) {
        if (attr === "r") {
            return "m"
        }
    },
    parentElement: head
}

meta = {
    content: content,
    r: "m",
    id: "K5MK4FPPNWrv",
    getAttribute(attr) {
        if (attr === "r") {
            return "m"
        }
    },
    parentNode: head
}
document = {
    addEventListener: function () {
    },
    attachEvent: function () {
    },
    createElement: function (ele) {
        console.log("document createElement ", ele)
        if (ele === "div") {
            return div
        }
        if (ele === "form") {
            return {}
        }
        if (ele === "a") {
            return {}
        }
    },
    getElementsByTagName(ele) {
        console.log("document getElementsByTagName ", ele)
        if (ele === "script") {
            return [script, script]
        }
        if (ele === "base") {
            return []
        }
    },
    getElementById(id) {
        console.log("document getElementById ", id)
        if (id === "K5MK4FPPNWrv") {
            return meta
        }
    }
}


location = {
    "ancestorOrigins": {},
    "href": "http://epub.cnipa.gov.cn/",
    "origin": "http://epub.cnipa.gov.cn",
    "protocol": "http:",
    "host": "epub.cnipa.gov.cn",
    "hostname": "epub.cnipa.gov.cn",
    "port": "",
    "pathname": "/",
    "search": "",
    "hash": ""
}

navigator = {}
setInterval = function () {
}
setTimeout = function () {
}


// 做一个代理监控
function setProxyArr(proxyObjArr) {
    for (let i = 0; i < proxyObjArr.length; i++) {
        const handler = `{
      get: function(target, property, receiver) {
        console.log("方法:", "get  ", "对象:", "${proxyObjArr[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", target[property], ", 属性值类型：", typeof target[property]);
        return target[property];
      },
      set: function(target, property, value, receiver) {
        console.log("方法:", "set  ", "对象:", "${proxyObjArr[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", value, ", 属性值类型：", typeof target[property]);
        return Reflect.set(...arguments);
      }
    }`;
        eval(`try {
            ${proxyObjArr[i]};
            ${proxyObjArr[i]} = new Proxy(${proxyObjArr[i]}, ${handler});
        } catch (e) {
            ${proxyObjArr[i]} = {};
            ${proxyObjArr[i]} = new Proxy(${proxyObjArr[i]}, ${handler});
        }`);
    }
}


setProxyArr(["window", "document", "div", "script", "head", "meta"])


'ts_js';
'auto_js';

function get_cookie() {
    return document.cookie
}


