export function ajax(url, instance) {
    $.ajax({
        url: url,
        success: function (data) {
            instance.tableUpdater(data);
        }
    });
}

export function sendAjax(instance, form) {
    const method = form.dataset.method.toUpperCase();
    // const method = form.data("method").toUpperCase();
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const input = form.querySelector('input');
        let data = new FormData(form);
        const url = form.action;

        let formResponse = $.ajax({
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
                instance.tableUpdater(data);
            }
        });
        formResponse.always(function (data, textStatus) {
            if (textStatus !== 'success') {
                let jData = JSON.parse(data.responseText);
                alert(jData['status']);
            }
        });
    });
}


