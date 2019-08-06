(function (jq) {
    jq('.multi-menu .title').click(function () {
        $(this).next().toggleClass('hide'); // 只控制当前菜单. 下方控制其他
        // $(this).next().removeClass('hide');
        // $(this).parent().siblings().find('.body').addClass('hide');
    });
})(jQuery);