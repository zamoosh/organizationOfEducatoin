import {getElement as select} from "./getElement.js";


const form = select('.form');

form.addEventListener('submit', (e) => {
    e.preventDefault()
    const input = select('.form input');
    let data = new FormData(form);
    const url = form.action;
    const method = form.data.method.toUpperCase();
    console.log(data)
    let ret = $.ajax({
        url: url,
        type: method,
        cache: false,
        processData: false,
        contentType: false,
        headers: {
            "X-CSRFToken": input.value
        },
        data: data,
        success: function (data) {
            console.log(data)

        }

    });
    ret.always(function (data, textStatus, jqXHR) {
        if (textStatus !== 'success') {
            jqXHR = data;
        }
        replaceContent(jqXHR.responseText);
    });


})

function replaceContent(content) {
    document.open();
    document.write(content);
    document.close();
}