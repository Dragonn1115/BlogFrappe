frappe.ready(function() {
	$(frm.fields_dict.text.input).css('height', '180px');

    })

// frappe.ui.form.on('Your DocType', {
//     onload: function(frm) {
//         if (frappe.session.user !== 'Guest') {
//             // 用户已登录
//             // 在这里添加修改sidebar的代码
//         }
//     }
// });