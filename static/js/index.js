// import {tableUpdater} from "./utils/tableUpdater.js";
//
// $(document).ready(function () {
//
//     $("#post").click(function () {
//         $.ajax({
//             url: "/lesson/save/lesson/",
//             type: "POST",
//             dataType: "json",
//             data: {
//                 'name': $('input[name="name"]').val(),
//                 'title': $('input[name="title"]').val(),
//                 'uni': $('input[name="uni"]').val()
//             },
//             success: function (data) {
//                 if ('status' in data) {
//                     if (data['status'] === 'failed') {
//                         alert('This lesson is already exist!');
//                     }
//                 } else {
//                     const element = $('.lesson-table')[0];
//                     tableUpdater(data, element);
//                 }
//             }
//         });
//     });
// })