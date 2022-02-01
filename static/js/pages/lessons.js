import './../utils/sidebar.js';
import swiperSlider from "./../utils/swiperSlider.js";
import {getElement as select} from "./../utils/getElement.js";
import "./../utils/fileUploader.js";
import {tableUpdater} from "../utils/tableUpdater.js";

window.addEventListener('DOMContentLoaded', () => {
    $.ajax({
        url: "/api_lesson/lessons/", success: function (data) {
            const element = $('.lesson-table')[0];
            tableUpdater(data, element);
        }
    });


});
//lesson page
const numbersOfSliders = select('.swiper-slide').length;
console.log(numbersOfSliders);
swiperSlider("#swiper-lesson", {slidesPerView: [1, 2, 3, 4], rows: 2, sliderNumbers: numbersOfSliders, loop: false});


$(document).ready(function () {
    // $("#post").click(function () {
    //     let img = document.querySelector('#files > input[type="file"]');
    //     $.ajax({
    //         url: "/lesson/save/lesson/",
    //         type: "POST",
    //         dataType: "json",
    //         data: {
    //             'name': $('input[name="name"]').val(),
    //             'title': $('input[name="title"]').val(),
    //             'uni': $('input[name="uni"]').val(),
    //             'image': $('input[name="image"]').val()
    //         },
    //         success: function (data) {
    //             if ('status' in data) {
    //                 if (data['status'] === 'failed') {
    //                     alert('This lesson is already exist!');
    //                 }
    //             } else {
    //                 const element = $('.lesson-table')[0];
    //                 tableUpdater(data, element);
    //             }
    //         }
    //     });
    // });

    // TODO(ZAMOOSH): I have to check if 'status' is in data or not to show the result...
    //     ask mostafa for that.
    const form = document.querySelector('.form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const input = document.querySelector('.form input');
        let data = new FormData($('.form').get(0));
        $.ajax({
            url: "/lesson/save/lesson/",
            type: "POST",
            cache: false,
            processData: false,
            contentType: false,
            mimeType: "multipart/form-data",
            headers: {
                "X-CSRFToken": input.value
            },
            data: data,
            success: function (data) {
                let c = 'status' in data;
                console.log(typeof c);
                if (c) {
                    console.log('status is in data');
                    // if (data['status'] === 'failed') {
                    //     alert('this lesson is already exist!');
                    // }
                }
            }
        });
    });
});