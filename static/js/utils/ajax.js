export function ajax(url, instance, element) {
    $.ajax({
        url: url,
        success: function (data) {
            instance.tableUpdater(data, element);
        }
    });
}

export function sendAjax(instance, form) {
    const method = form.dataset.method.toUpperCase();
    const url = form.action;
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


