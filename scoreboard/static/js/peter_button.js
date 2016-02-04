/*
 * 定义了各种功能的按钮
 * switch-button:
 * 由一个button和一个input组成
 * <button class="switch-button" type="button">Text</button>
 * <input type="hidden" name="input_name" value="1">
 * 自定义切换式的按钮,每个按钮对应一个input hidden来记录按钮的状态
 * 表单提交时会发送1或0到服务器
 *
 * checkbox-button
 * 由一个label和一个input组成
 * <label for="input_id" class="checkbox-button">Text</label>
 * <input id="input_id" type="checkbox" name="input_name" value="input_value" class="hidden" checked>
 * 自定义checkbox式的按钮,每个按钮保存有是否选中的状态和按钮的值
 * 表单提交时不会提交未选中按钮的值到服务器
 */

$(function () {
    // 切换式按钮
    var switchButtons = $("button.switch-button");
    // 初始化切换式按钮的class和value
    switchButtons.each(function () {
        var hiddenInput = $(this).siblings("input[type='hidden']");
        $(this).addClass("btn");
        if (hiddenInput.val() == 1) {
            $(this).addClass("btn-success");
        } else {
            $(this).addClass("btn-default");
            hiddenInput.val(0);
        }
    });
    // 定义这类按钮的click事件
    switchButtons.click(function () {
        var hiddenInput = $(this).next("input[type='hidden']");
        if (hiddenInput.val() == 1) {
            $(this).removeClass("btn-success").addClass("btn-default");
            hiddenInput.val(0);
        } else {
            $(this).removeClass("btn-default").addClass("btn-success");
            hiddenInput.val(1);
        }
    });

    // checkbox式按钮
    var checkboxButtons = $("label.checkbox-button");
    // 初始化checkbox按钮的class
    checkboxButtons.each(function () {
        var checkbox = $(this).next("input[type='checkbox']");
        $(this).addClass('btn');
        if (checkbox.prop('checked')) {
            $(this).addClass('btn-success');
        } else {
            $(this).addClass('btn-default');
        }
    });
    // 定义这类按钮的click事件
    checkboxButtons.click(function () {
        // 因为click事件是在checkbox改变状态之前,所以取到的checked状态是之前的状态
        var checkbox = $(this).next("input[type='checkbox']");
        if (checkbox.prop('checked')) {
            $(this).removeClass("btn-success").addClass("btn-default");
        } else {
            $(this).removeClass("btn-default").addClass("btn-success");
        }
    });
});
