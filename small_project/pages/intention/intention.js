// pages/intention/intention.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        manager_array: ['请选择销售经理', '张三', '王五', '赵六', '李四'],
        project_array: ['请选择项目类型', '直销', '代理', '专项(事业部)'],
        market_array: ['请选择市场类型', '高校','高职','中职','K12','幼儿园','机构','政府','代理','海外'],
        manager_index: 0,
        project_index: 0,
        market_index: 0,
        date: '2019-04-03',
        current_swiper: 0,
        color1: "#f34573",
        color2: "#e6e6e6",
        color3: "#e6e6e6",
        font1: "#f34573",
        font2: "",
        font3: "",
        form_value: {},
    },
    /**
     * 表单提交
     */
    submitform: function (e) {
        console.log("form提交点击事件执行")
        var that = this;
        console.log(e)
    },
    /**
     * 表单提交点击事件
     */
    submit_form_btn: function (e) {
        console.log("btn点击事件执行")
        this.submitform(e)
    },
    /**
     * 存值函数
     */
    savevalue: function (parm, index) {
        var value_arr = this.data.form_value;
        value_arr[parm] = index;
        this.setData({
            form_value: value_arr
        })
        console.log(this.data.form_value)
    },
    /**
     *合作内容 
     */

    /**
     * 客户名称
     */

    /**
     * 采购形式
     */
    /**
     * 市场类型
     */
    market_bindPickerChange: function(e){
        this.setData({
            market_index: e.detail.value
        })
    },

    /**
     * 项目类型选择
     */
    project_bingPickerChange(e) {
        this.setData({
            project_index: e.detail.value
        })
        this.savevalue('project_type', this.data.project_index)
    },
    /**
     * 项目经理选择
     */
    manager_bindPickerChange(e) {
        // console.log('picker发送选择改变，携带值为', e.detail.value)
        this.setData({
            manager_index: e.detail.value
        });
        this.savevalue('manager', this.data.manager_index)
    },
    /**
     * 日期选择控件
     */
    bindDateChange(e) {
        this.setData({
            date: e.detail.value
        })
    },
    /**
     * 头部进程颜色变换
     */
    selectcolor: function (next_index) {
        if (next_index == 0) {
            this.setData({
                color1: "#f34573",
                color2: "#e6e6e6",
                color3: "#e6e6e6",
                font1: "#f34573",
                font2: "",
                font3: "",
            })
        } else if (next_index == 1) {
            this.setData({
                color2: "#f34573",
                color1: "#e6e6e6",
                color3: "#e6e6e6",
                font2: "#f34573",
                font1: "",
                font3: "",
            })
        } else {
            this.setData({
                color3: "#f34573",
                color1: "#e6e6e6",
                color2: "#e6e6e6",
                font3: "#f34573",
                font1: "",
                font2: "",
            })
        }

    },
    /**
     * 下一页swiper
     */
    next_swiper: function (e) {
        var next_index = this.data.current_swiper + 1;
        if (next_index < 3) {
            this.setData({
                current_swiper: next_index,
            })
            this.selectcolor(next_index);
        };



    },
    /**
     * 上一页swiper
     */
    pre_swiper: function (e) {
        var pre_index = this.data.current_swiper - 1;
        console.log(pre_index)
        if (pre_index >= 0) {
            this.setData({
                current_swiper: pre_index
            })
            this.selectcolor(pre_index);
        } else {
            this.setData({
                current_swiper: 0,
            })
        }

    },
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {

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