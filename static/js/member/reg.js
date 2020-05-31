;
var member_reg_ops = {
    init: function(){
        this.eventBind();
    },
    eventBind: function () {
        $('.reg_wrap .do-reg').click(function () {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")){
                common_ops.alert("正在处理，请不要重复点击");
            }
            btn_target.addClass("disabled");
            var log_name = $('.reg_wrap input[name=login_name]').val();
            var log_pwd = $('.reg_wrap input[name=login_pwd]').val();
            var re_pwd = $('.reg_wrap input[name=login_repwd]').val();
            if (log_name === undefined){
                common_ops.alert("请输入账号~");
                return;
            }
            if (log_pwd === undefined || log_pwd.length < 6) {
                common_ops.alert("请输入密码，且密码不小于6个字符~");
                return;
            }
            if (re_pwd === undefined || re_pwd != log_pwd) {
                common_ops.alert("两次输入的密码不一致");
                return;
            }
            $.ajax({
                url:common_ops.buildUrl("/user/reg"),
                type: "POST",
                data:{
                    "log_name": log_name,
                    "log_pwd": log_pwd,
                    "re_pwd": re_pwd
                },
                dataType: "json",
                success: function (res) {
                    btn_target.removeClass("disabled")
                    callBackFun = null;
                    if (res["code"] === 200){
                        callBackFun = function(){
                            window.location.href = common_ops.buildUrl("/index")
                        }
                    }
                    common_ops.alert(res['msg'], callBackFun)

                }

            });
        });
    }
};

$(document).ready(function () {
    member_reg_ops.init();
});