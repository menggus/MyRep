// pages/login/login.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        orhidden:"display:none",
        tsusername:"18574380075",
        tspassword:"123456"
    },
    /**
     * 账号与密码的校验
     */
    check_username: function(e){
        var username = e.detail.value
        var len = username.length
        if (len!==6){
            wx.showToast({
                title: '请输入工号',
                icon: 'none',
                mask: 'true',
                duration: 2000
            })
        }
    },
    check_password: function(e){
        var username = e.detail.value
        var len = username.length
        if (len<6 || len>20) {
            wx.showToast({
                title: '密码长度错误,长度为6-20位（字母、数字、下划线等）',
                icon: 'none',
                mask: 'true',
                duration: 2000
            })
        }
    },
    /**
     * 登录
     */
    login: function (e) {
        // 获取user信息进行校验
        var username = e.detail.value.username;
        var password = e.detail.value.password;
        console.log(username + ":" + password);
        if (username=="" || password=="") {
            console.log("账号密码不完整")
            this.setData({
                errormsg: "账号密码不完整"
            })
            return
        };
        // // 远程服务端校验
        // wx.request({
        //     url: 'www.****',
        //     data:{
        //         username:username,
        //         password:password
        //     },
        //     // 回调函数，返回信息res
        //     success: function(res){
        //         // 对返回信息进行识别，校验
        //     },
        // });
        if (username == this.data.tsusername && password == this.data.tspassword) {
            // username == this.data.tsusername && password == this.data.tspassword
            wx.redirectTo({
                url: '../crm/crm',
            })
        } else {
            this.setData({
                errormsg:"账号或密码错误"
            })
            console.log("账号密码不正确")
        }

    },

    /**
     * 输入框获取焦点时，移除提示信息
     * 
     */
    removetip: function () {
        this.setData({
            errormsg: ""
        })
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        wx.clearStorageSync();   //清除缓存
    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {

    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function () {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    }
})