// pages/predict/predict.js
Page({
  /**
   * 页面的初始数据
   */
  data: {
    order_id: 'SP20190300000775',
    area_id:"豫晋苏",
    province_id:"河南",
    marking_type_id:"公办中职",
    purchase_form:"招投标",
    product_line_type:"金融产品线",
    manager:"张三",
    customer:"河南科技有限公司"
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
      wx.setNavigationBarTitle({
        title: '国泰安每周合同预测',
      })
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