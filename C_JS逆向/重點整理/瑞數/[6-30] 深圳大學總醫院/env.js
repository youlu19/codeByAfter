
content="YhOCeYUxjtW0_3GhaeiImfzasDW.fp0FTUA6jyh6YkpA_7xlkkdmEPD4c8c3ftdfmKsyYl24xlV3euMcDrJSRWCeUZtRfZAL.fOXLwDR0YzADhgKn63s09mfOZ7xoQMhNdy547W4NgCJb0tb25XfHUH2XGRIN2P8eqLGp3XIca9B84vNVcJJRNby1rg2HXZez1DvxKi.efV"
// delete __dirname
// delete __filename

window =top = self= global;
window.addEventListener = function () {
}
window.XMLHttpRequest = function (){}

// delete global
// delete Buffer

meta = {
    0: {
        /* "http-equiv":"Content-Type",
         "content":"text/html; charset=utf-8",*/
    },
    1: {
        "content": content,
        parentNode: {
            removeChild() {
            }
        }
    },
    length: 2
}
// document = {
//
//     // removeChild: function () {
//     //
//     // }
//
//
//     // createElement(ele) {
//     //     console.log("document createElement:", ele)
//     //     if (ele === "div") {
//     //         return {
//     //             getElementsByTagName: function () {
//     //                 return []
//     //             }
//     //         }
//     //     }
//     //
//     // },
//     // getElementsByTagName(ele) {
//     //     console.log("document getElementsByTagName:", ele)
//     //     if (ele === "meta") {
//     //         return meta
//     //     }else if(ele==="base"){
//     //         return []
//     //     }else if(ele==="script"){
//     //         return []
//     //     }
//     //
//     // },
//     // getElementById() {
//     // },
//     // addEventListener: function () {
//     // },
//     // documentElement: {
//     //     addEventListener: function () {
//     //     }
//     // }
//
// }
location = {
    "ancestorOrigins": {},
    "href": "https://sugh.szu.edu.cn/Html/News/Columns/7/Index.html",
    "origin": "https://sugh.szu.edu.cn",
    "protocol": "https:",
    "host": "sugh.szu.edu.cn",
    "hostname": "sugh.szu.edu.cn",
    "port": "",
    "pathname": "/Html/News/Columns/7/Index.html",
    "search": "",
    "hash": ""
}
navigator = {}
history = {}
screen = {}

setInterval =function (){}
setTimeout =function (){}


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


setProxyArr(["window", "document", "location", "script", "head", "meta"])