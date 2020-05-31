;

var member_login_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $('.login_wrap .do-login').click(function () {
            var btn_login = $(this);
            if ( btn_login.hasClass('disabled') ){
              common_ops.alert("正在处理，请不要重复点击");
            }
            btn_login.addClass("disabled");
            var login_name = $('.login_wrap input[name=login_name]').val();
            var login_pwd = $('.login_wrap input[name=login_pwd]').val();

            if (login_name === undefined){
              common_ops.alert("请输入账号~");
              return;
            }
            if (login_pwd === undefined || login_pwd.length < 6) {
              common_ops.alert("请输入密码，且密码不小于6个字符~");
              return;
            }
            $.ajax({
                url:common_ops.buildUrl("/user/login"),
                type: "POST",
                data:{
                    "login_name": login_name,
                    "login_pwd": login_pwd,
                },
                dataType: "json",
                success: function (res) {
                    btn_login.removeClass("disabled")
                    callBackFun = null;
                    if (res["code"] === 200){
                        callBackFun = function(){
                            window.location.href = common_ops.buildUrl("/index")
                        }
                    }
                    common_ops.alert(res['msg'], callBackFun)

                }

            });
        })
    }

};

$(document).ready(function () {
    member_login_ops.init();
    member_login_ops.eventBind();
});